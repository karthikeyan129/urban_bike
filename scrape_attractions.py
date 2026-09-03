import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://english.visitseoul.net/"
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(URL, headers=headers, timeout=20).text
soup = BeautifulSoup(html, "html.parser")

rows = []
for a in soup.find_all("a", href=True):
    name = a.get_text(" ", strip=True)
    href = a.get("href")
    if name and len(name) > 2:
        rows.append({"Attraction": name, "URL": href})

pd.DataFrame(rows).drop_duplicates().to_csv("seoul_attractions.csv", index=False)
print("Created seoul_attractions.csv")
