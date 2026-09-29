
import requests
from bs4 import BeautifulSoup
import csv
import os

# Save the CSV file in the same folder as this Python file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Website to scrape
url = "https://quotes.toscrape.com/"

try:
    # Send a request to the website
    response = requests.get(url, timeout=15)

    # Check whether the request was successful
    response.raise_for_status()

    # Parse the website HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes on the page
    quotes = soup.find_all("div", class_="quote")

    # Create a CSV file
    with open(
        "quotes.csv", "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write column headings
        writer.writerow(["Quote", "Author", "Tags"])

        # Extract and save each quote
        for quote in quotes:
            quote_text = quote.find(
                "span", class_="text"
            ).get_text(strip=True)

            author = quote.find(
                "small", class_="author"
            ).get_text(strip=True)

            tags = [
                tag.get_text(strip=True)
                for tag in quote.find_all(
                    "a", class_="tag"
                )
            ]

            writer.writerow([
                quote_text,
                author,
                ", ".join(tags)
            ])

    print("Web scraping completed successfully!")
    print("Total quotes collected:", len(quotes))
    print("Data saved in quotes.csv")

except requests.exceptions.RequestException as error:
    print("Website connection error:", error)

except Exception as error:
    print("An error occurred:", error)
