"""Market scan for Merkado social: our own price history and ranked listing picks.

Reads only public merkado.cw API endpoints. Standard library only, so it runs in
any cloud session without installs.

  python scripts/market_scan.py snapshot      # save today's prices, log changes
  python scripts/market_scan.py picks car     # ranked car candidates with reasons
  python scripts/market_scan.py picks home    # ranked real-estate candidates
  python scripts/market_scan.py roundup car under-15000 5   # one listing per seller
  python scripts/market_scan.py roundup home pool 5         # one listing per agency
  python scripts/market_scan.py themes                      # list all themes
  python scripts/market_scan.py featured                    # paid Featured cars and their social post

Paid Featured cars come first, then bargains: people on Curaçao love a bargain
(Product Lead, 28 and 30 Oct 2026).

State lives in state/market/:
  cars.csv, homes.csv     latest snapshot, with first_seen per listing
  price-changes.csv       append-only log of price changes we observed
"""

import csv
import datetime as dt
import json
import re
import statistics
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state" / "market"
POSTS = ROOT / "state" / "posts.csv"
SITE = "https://merkado.cw"
TODAY = dt.date.today().isoformat()

SNAP_FIELDS = ["slug", "price", "seller", "origin", "published_at", "first_seen", "last_seen"]
CHANGE_FIELDS = ["date", "kind", "slug", "old_price", "new_price", "seller"]


def get_json(path):
    req = urllib.request.Request(SITE + path, headers={"User-Agent": "merkado-socials/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_cars():
    cars, page = [], 1
    while True:
        batch = get_json(f"/api/cars?sort=newest&page={page}").get("listings", [])
        if not batch:
            return cars
        cars += batch
        page += 1
        if page > 60:
            return cars


def fetch_homes():
    return get_json("/api/real-estate/map").get("listings", [])


def seller(item):
    return item.get("source_name") or ("native" if item.get("listing_origin") != "scraped" else "")


def price_of(item, kind):
    p = item.get("price") if kind == "car" else item.get("price_xcg")
    return int(p) if p else 0


def read_csv(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def snapshot():
    changes_path = STATE / "price-changes.csv"
    changes = read_csv(changes_path)
    for kind, items, name in (("car", fetch_cars(), "cars.csv"), ("home", fetch_homes(), "homes.csv")):
        old = {r["slug"]: r for r in read_csv(STATE / name)}
        rows = []
        for it in items:
            slug, price = it["slug"], price_of(it, kind)
            prev = old.get(slug)
            if prev and prev["price"] and price and int(prev["price"]) != price:
                changes.append({"date": TODAY, "kind": kind, "slug": slug, "old_price": prev["price"],
                                "new_price": price, "seller": seller(it)})
            rows.append({"slug": slug, "price": price, "seller": seller(it), "origin": it.get("listing_origin", ""),
                         "published_at": (it.get("published_at") or "")[:10],
                         "first_seen": prev["first_seen"] if prev else TODAY, "last_seen": TODAY})
        write_csv(STATE / name, SNAP_FIELDS, rows)
        print(f"{kind}: {len(rows)} live, {len(old)} in last snapshot")
    write_csv(changes_path, CHANGE_FIELDS, changes)
    print(f"price changes logged: {sum(1 for c in changes if c['date'] == TODAY)} today, {len(changes)} total")


def recent_post_slugs(days=30):
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    return {r["listing_slug"] for r in read_csv(POSTS) if r.get("listing_slug") and r.get("date", "") >= cutoff}


def price_drops(kind, days=30):
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    drops = {}
    for c in read_csv(STATE / "price-changes.csv"):
        if c["kind"] == kind and c["date"] >= cutoff and int(c["new_price"]) < int(c["old_price"]):
            drops[c["slug"]] = c
    return drops


def days_since(date_str):
    try:
        return (dt.date.today() - dt.date.fromisoformat(date_str[:10])).days
    except ValueError:
        return 999


def data_flags(c):
    """Reasons a car's data cannot be trusted without a source check."""
    flags = []
    years_in_slug = {int(y) for y in re.findall(r"(?<!\d)(19[89]\d|20[0-4]\d)(?!\d)", c["slug"])}
    if years_in_slug and c["year"] not in years_in_slug:
        flags.append(f"slug says {sorted(years_in_slug)}, listing says {c['year']}")
    km = c.get("mileage")
    if not km:
        flags.append("no mileage")
    elif km < 1000 and c["year"] < dt.date.today().year - 1:
        flags.append(f"implausible mileage {km} km")
    elif km % 1000 == 123:
        flags.append(f"mileage {km} km looks like a placeholder")
    return flags


def featured_until(c):
    """End of a paid Featured week (UTC) while it is still running, else None."""
    raw = c.get("featured_until")
    if not raw:
        return None
    try:
        until = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    return until if until > dt.datetime.now(dt.timezone.utc) else None


def featured_report():
    """Cars Featured right now, and whether social already gave them their post this Featured week."""
    rows = read_csv(POSTS)
    found = False
    for c in fetch_cars():
        until = featured_until(c)
        if not until or c.get("status") != "active":
            continue
        found = True
        start = (until - dt.timedelta(days=7)).date().isoformat()
        done = [r for r in rows if r.get("listing_slug") == c["slug"] and r.get("date", "") >= start]
        state = "posted " + ", ".join(r["post_id"] for r in done) if done else "NEEDS A POST before " + f"{until:%d %b}"
        print(f"{c['year']} {c['make']} {c['model']} | XCG {c.get('price')} | {seller(c)} | {c['slug']} | "
              f"Featured until {until:%d %b %H:%M} UTC | {state}")
    if not found:
        print("No Featured cars right now.")


def rank_cars():
    cars = [c for c in fetch_cars() if c.get("status") == "active" and c.get("price") and c.get("year")]
    posted, drops = recent_post_slugs(), price_drops("car")
    groups = defaultdict(list)
    norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
    for c in cars:
        groups[(norm(c["make"]), norm(c["model"]))].append(c)
    cheapest = {}
    for c in cars:
        body = c.get("body_type")
        if body and not data_flags(c) and (body not in cheapest or c["price"] < cheapest[body]["price"]):
            cheapest[body] = c
    ranked = []
    for c in cars:
        until = featured_until(c)
        # A Featured car stays eligible during its paid week even if we posted it before.
        if (c["slug"] in posted and not until) or not (c.get("primary_image_url") or c.get("primary_image_path")):
            continue
        score, why = 0, []
        flags = data_flags(c)
        if until:
            score += 100; why.append(f"FEATURED until {until:%d %b %H:%M} UTC: post it during its Featured week")
        if c.get("listing_origin") != "scraped":
            score += 30; why.append("native listing")
        age = days_since(c.get("published_at") or "")
        if age <= 7:
            score += 20; why.append(f"just added ({age} d)")
        elif age <= 14:
            score += 10; why.append(f"new ({age} d)")
        if c["slug"] in drops:
            d = drops[c["slug"]]
            score += 35; why.append(f"price drop XCG {d['old_price']} to {d['new_price']} ({d['date']})")
        comps = [o for o in groups[(norm(c["make"]), norm(c["model"]))]
                 if o is not c and abs(o["year"] - c["year"]) <= 2 and not data_flags(o)]
        if len(comps) >= 4 and not flags:
            med = statistics.median(o["price"] for o in comps)
            if c["price"] <= med * 0.9:
                score += 20; why.append(f"XCG {int(med - c['price'])} below the median of {len(comps)} similar")
        if cheapest.get(c.get("body_type")) is c:
            score += 12; why.append(f"cheapest {c['body_type']} on Merkado")
        if c["price"] < 10000:
            score += 14; why.append("under XCG 10.000")
        elif c["price"] < 15000:
            score += 8; why.append("under XCG 15.000")
        text = f"{c.get('trim') or ''} {c.get('title') or ''}".lower()
        if c.get("body_type") == "Van & MPV" or "7 seat" in text or "7-seat" in text:
            score += 6; why.append("family, 7 seats")
        if c.get("fuel_type") in ("electric", "hybrid"):
            score += 6; why.append(c["fuel_type"])
        if c.get("body_type") == "Pickup & Truck":
            score += 4; why.append("pickup")
        if flags:
            score -= 40; why.append("CHECK: " + "; ".join(flags))
        ranked.append((score, c, why))
    ranked.sort(key=lambda r: -r[0])
    return ranked


def print_car(score, c, why):
    print(f"{score:>4} | {c['year']} {c['make']} {c['model']} | XCG {c['price']} | {c.get('mileage') or '?'} km | "
          f"{seller(c)} | {c['slug']} | {', '.join(why)}")


def car_picks(limit):
    for score, c, why in rank_cars()[:limit]:
        print_car(score, c, why)


THEMES = {
    "just-added": lambda c: days_since(c.get("published_at") or "") <= 7,
    "under-10000": lambda c: c["price"] < 10000,
    "under-15000": lambda c: c["price"] < 15000,
    "under-20000": lambda c: c["price"] < 20000,
    "price-drop": lambda c: c["slug"] in price_drops("car"),
    "electric": lambda c: c.get("fuel_type") in ("electric", "hybrid"),
    "family": lambda c: c.get("body_type") == "Van & MPV" or "7 seat" in f"{c.get('trim') or ''} {c.get('title') or ''}".lower(),
    "suv": lambda c: c.get("body_type") == "SUV & Crossover",
    "pickup": lambda c: c.get("body_type") == "Pickup & Truck",
    "nearly-new": lambda c: c["year"] >= dt.date.today().year - 2,
}

HOME_THEMES = {
    "just-added": lambda h: days_since(h.get("published_at") or "") <= 7,
    "rent-under-3000": lambda h: h.get("listing_type") == "rent" and h["price_xcg"] <= 3000,
    "sale-under-500000": lambda h: h.get("listing_type") == "sale" and h["price_xcg"] <= 500000,
    "pool": lambda h: any(w in f"{h.get('title') or ''} {h.get('display_title') or ''}".lower() for w in ("pool", "zwembad")),
    "beach-areas": lambda h: h.get("neighbourhood") in ("Jan Thiel", "Blue Bay", "Piscadera", "Mambo", "Westpunt"),
    "price-drop": lambda h: h["slug"] in price_drops("home"),
}


def car_roundup(theme, limit):
    """Best clean listing per seller for a theme: a carousel never shows the same seller twice."""
    seen, out = set(), []
    for score, c, why in rank_cars():
        if not THEMES[theme](c) or any(w.startswith("CHECK") for w in why):
            continue
        if seller(c) in seen:
            continue
        seen.add(seller(c)); out.append((score, c, why))
        if len(out) == limit:
            break
    for row in out:
        print_car(*row)
    if len(out) < 3:
        print(f"Only {len(out)} sellers qualify for '{theme}': pick another theme or post a single.")


def home_roundup(theme, limit):
    """Best home per agency for a theme: a carousel never shows the same agency twice."""
    homes = [h for h in fetch_homes() if h.get("status") == "active" and h.get("price_xcg") and h.get("primary_image_url")]
    posted = recent_post_slugs()
    homes = [h for h in homes if h["slug"] not in posted and HOME_THEMES[theme](h) and h.get("bedrooms")]
    homes.sort(key=lambda h: (h["slug"] not in price_drops("home"), days_since(h.get("published_at") or ""), h["price_xcg"]))
    seen, out = set(), []
    for h in homes:
        if seller(h) in seen:
            continue
        seen.add(seller(h)); out.append(h)
        if len(out) == limit:
            break
    for h in out:
        print(f"{h.get('listing_type')} {h.get('real_estate_type')} {h.get('bedrooms')} bd | XCG {h['price_xcg']} | "
              f"{h.get('neighbourhood')} | {seller(h)} | {h['slug']} | {days_since(h.get('published_at') or '')} d")
    if len(out) < 3:
        print(f"Only {len(out)} agencies qualify for '{theme}': pick another theme.")


def home_picks(limit):
    homes = [h for h in fetch_homes() if h.get("status") == "active" and h.get("price_xcg")]
    posted, drops = recent_post_slugs(), price_drops("home")
    top_hoods = {"Blue Bay", "Jan Thiel", "Otrobanda", "Brakkeput", "Piscadera", "Jan Sofat"}
    ranked = []
    for h in homes:
        if h["slug"] in posted or not h.get("primary_image_url"):
            continue
        score, why = 0, []
        if h.get("listing_origin") != "scraped":
            score += 30; why.append("native listing")
        age = days_since(h.get("published_at") or "")
        if age <= 7:
            score += 20; why.append(f"just added ({age} d)")
        elif age <= 14:
            score += 10; why.append(f"new ({age} d)")
        if h["slug"] in drops:
            d = drops[h["slug"]]
            score += 25; why.append(f"price drop XCG {d['old_price']} to {d['new_price']} ({d['date']})")
        if h.get("neighbourhood") in top_hoods:
            score += 5; why.append(f"popular area {h['neighbourhood']}")
        if h.get("listing_type") == "rent" and h["price_xcg"] <= 3000:
            score += 6; why.append("rent under XCG 3.000")
        if h.get("real_estate_type") in ("house", "apartment", "villa") and h.get("bedrooms"):
            score += 4
        else:
            score -= 10; why.append("CHECK: type or bedrooms missing")
        if not h.get("latitude"):
            why.append("no map pin")
        ranked.append((score, h, why))
    ranked.sort(key=lambda r: -r[0])
    for score, h, why in ranked[:limit]:
        print(f"{score:>4} | {h.get('listing_type')} {h.get('real_estate_type')} {h.get('bedrooms')} bd | "
              f"XCG {h['price_xcg']} | {h.get('neighbourhood')} | {seller(h)} | {h['slug']} | {', '.join(why)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if args[:1] == ["snapshot"]:
        snapshot()
    elif args[:1] == ["picks"] and args[1:2] in (["car"], ["home"]):
        n = int(args[2]) if len(args) > 2 else 12
        (car_picks if args[1] == "car" else home_picks)(n)
    elif args[:2] == ["roundup", "car"] and len(args) > 2 and args[2] in THEMES:
        car_roundup(args[2], int(args[3]) if len(args) > 3 else 5)
    elif args[:2] == ["roundup", "home"] and len(args) > 2 and args[2] in HOME_THEMES:
        home_roundup(args[2], int(args[3]) if len(args) > 3 else 5)
    elif args[:1] == ["featured"]:
        featured_report()
    elif args[:1] == ["themes"]:
        print("car:", ", ".join(THEMES)); print("home:", ", ".join(HOME_THEMES))
    else:
        print(__doc__)
