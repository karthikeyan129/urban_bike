import csv
import time
from urllib.parse import urljoin
import os

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://english.visitseoul.net"
LIST_URL = "https://english.visitseoul.net/attractions"
OUTPUT_CSV = "data/seoul_attractions.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Bot/1.0; +https://github.com/yourname)"
}


def fetch_page(url):
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_list_page(html, base):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    # Try a few common list/card selectors; site layout may change.
    cards = soup.select(".list_contents .txt_area") or soup.select(".attraction_list .info") or soup.select(".card") or soup.select("a")
    for c in cards:
        name_tag = c.select_one("h4 a") or c.select_one("h4") or c.select_one(".tit") or (c if c.name == "a" else None)
        if not name_tag:
            continue
        name = name_tag.get_text(strip=True)
        if not name or len(name) < 4:
            continue
        link = None
        if getattr(name_tag, 'has_attr', None) and name_tag.has_attr("href"):
            link = urljoin(base, name_tag["href"])
        else:
            href = c.get("href")
            if href:
                link = urljoin(base, href)
        category_tag = c.select_one(".cate") or c.select_one(".category")
        category = category_tag.get_text(strip=True) if category_tag else ""
        area_tag = c.select_one(".area") or c.select_one(".location")
        area = area_tag.get_text(strip=True) if area_tag else ""
        results.append({"Attraction": name, "Category": category, "Area": area, "URL": link or ""})
    return results


def enrich_and_collect(items, limit=200):
    seen = set()
    rows = []
    for it in items:
        key = (it["Attraction"], it["URL"])
        if key in seen:
            continue
        seen.add(key)
        rows.append(it)
        if len(rows) >= limit:
            break
    return rows


def main():
    html = fetch_page(LIST_URL)
    items = parse_list_page(html, BASE_URL)
    if len(items) < 10:
        soup = BeautifulSoup(html, "html.parser")
        anchors = soup.select("a[href*='/attractions/']")
        for a in anchors:
            name = a.get_text(strip=True)
            href = a.get("href")
            if name:
                items.append({"Attraction": name, "Category": "", "Area": "", "URL": urljoin(BASE_URL, href)})
    items = enrich_and_collect(items, limit=300)
    # De-duplicate by name
    unique = []
    seen_names = set()
    for it in items:
        if it["Attraction"] not in seen_names:
            seen_names.add(it["Attraction"])
            unique.append(it)
    final = []
    for it in unique:
        if len(final) >= 50:
            break
        try:
            if it["URL"]:
                page = fetch_page(it["URL"])
                ps = BeautifulSoup(page, "html.parser")
                cat = ps.select_one(".category") or ps.select_one(".cate")
                area = ps.select_one(".area") or ps.select_one(".location")
                it["Category"] = cat.get_text(strip=True) if cat else it["Category"]
                it["Area"] = area.get_text(strip=True) if area else it["Area"]
                time.sleep(0.8)
        except Exception:
            pass
        final.append(it)
        if len(final) >= 10:
            break
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Attraction", "Category", "Area", "URL"])
        writer.writeheader()
        for r in final:
            writer.writerow(r)
    print(f"Wrote {len(final)} attractions to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
