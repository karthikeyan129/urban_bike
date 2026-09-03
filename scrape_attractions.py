import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


BASE_URL = "https://english.visitseoul.net"
URL = "https://english.visitseoul.net/attractions"

OUTPUT_FILE = "seoul_attractions.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_attractions():

    print("Connecting to Visit Seoul...")

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    rows = []

    # --------------------------------------------------------
    # Find attraction links
    # --------------------------------------------------------

    for link in soup.find_all("a", href=True):

        name = link.get_text(
            " ",
            strip=True
        )

        href = link.get("href")

        if not name:
            continue

        # Keep meaningful attraction names.
        # Very short navigation labels are ignored.
        if len(name) < 4:
            continue

        full_url = urljoin(
            BASE_URL,
            href
        )

        # Visit Seoul attraction pages normally contain
        # "/attractions/" in their URL.
        if "/attractions/" not in full_url:
            continue

        rows.append({
            "Attraction": name,
            "URL": full_url
        })


    # --------------------------------------------------------
    # Remove duplicates
    # --------------------------------------------------------

    result = pd.DataFrame(rows)

    if result.empty:
        raise RuntimeError(
            "No attraction records were found. "
            "The Visit Seoul page structure may have changed."
        )

    result = result.drop_duplicates(
        subset=["Attraction", "URL"]
    )


    # --------------------------------------------------------
    # Extract category and area from individual pages
    # --------------------------------------------------------

    final_rows = []

    for index, row in result.iterrows():

        if len(final_rows) >= 10:
            break

        try:

            print(
                f"Scraping {len(final_rows) + 1}/10: "
                f"{row['Attraction']}"
            )

            page_response = requests.get(
                row["URL"],
                headers=HEADERS,
                timeout=20
            )

            page_response.raise_for_status()

            page_soup = BeautifulSoup(
                page_response.text,
                "html.parser"
            )

            text = page_soup.get_text(
                " ",
                strip=True
            )

            category = "Unknown"
            area = "Unknown"

            # ------------------------------------------------
            # Category
            # ------------------------------------------------

            known_categories = [
                "Landmark",
                "Palaces",
                "Historical Sites",
                "Galleries & Museums",
                "Market",
                "Park & Garden",
                "Nature",
                "Shopping",
                "Entertainment"
            ]

            for item in known_categories:

                if item.lower() in text.lower():
                    category = item
                    break


            # ------------------------------------------------
            # Area
            # ------------------------------------------------

            known_areas = [
                "Gwanghwamun",
                "Myeongdong",
                "Dongdaemun",
                "Hongdae",
                "Yeouido",
                "Itaewon",
                "Gangnam",
                "Jamsil"
            ]

            for item in known_areas:

                if item.lower() in text.lower():
                    area = item
                    break


            final_rows.append({
                "Attraction": row["Attraction"],
                "Category": category,
                "Area": area,
                "URL": row["URL"]
            })


        except requests.RequestException as error:

            print(
                f"Skipped {row['Attraction']}: {error}"
            )

        except Exception as error:

            print(
                f"Error processing {row['Attraction']}: {error}"
            )


    # --------------------------------------------------------
    # Save output
    # --------------------------------------------------------

    output = pd.DataFrame(final_rows)

    if len(output) < 10:
        raise RuntimeError(
            f"Only {len(output)} attractions were collected. "
            "At least 10 are required by the assignment."
        )

    output.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print(
        f"\nSuccessfully saved {len(output)} "
        f"attractions to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    scrape_attractions()
