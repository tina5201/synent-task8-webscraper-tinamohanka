"""
Task 8: Web Scraper
Synent Technologies - Python Development Internship
Author: Your Name

Scrapes book data from https://books.toscrape.com
(Free, legal practice website - no API key needed)
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import os


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}


# ─────────────────────────────────────────────
#  Scraper
# ─────────────────────────────────────────────
def scrape_page(page_num):
    """Scrape a single page and return list of book dicts."""
    url = BASE_URL.format(page_num)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection. Please check your network.")
        return None
    except requests.exceptions.Timeout:
        print(f"❌ Request timed out for page {page_num}.")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title  = article.h3.a["title"]
        price  = article.select_one(".price_color").text.strip()
        rating_word = article.p["class"][1]
        rating = RATING_MAP.get(rating_word, 0)
        availability = article.select_one(".availability").text.strip()

        books.append({
            "title":        title,
            "price":        price,
            "rating":       rating,
            "availability": availability,
        })

    return books


def scrape_books(num_pages=1, min_rating=1, max_price=None):
    """Scrape multiple pages with optional filters."""
    all_books = []
    print(f"\n🔍 Scraping {num_pages} page(s)...\n")

    for page in range(1, num_pages + 1):
        print(f"  📄 Scraping page {page}/{num_pages}...", end=" ")
        books = scrape_page(page)

        if books is None:   # connection error
            break
        if not books:       # empty page / end of site
            print("No more pages found.")
            break

        # Apply filters
        for book in books:
            price_num = float(book["price"].replace("£", "").replace("Â", "").strip())
            if book["rating"] < min_rating:
                continue
            if max_price and price_num > max_price:
                continue
            all_books.append(book)

        print(f"✅ {len(books)} books found")

    return all_books


# ─────────────────────────────────────────────
#  Save Functions
# ─────────────────────────────────────────────
def save_json(books, filename="books.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)
    print(f"✅ Saved {len(books)} books to '{filename}'")


def save_csv(books, filename="books.csv"):
    if not books:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        writer.writerows(books)
    print(f"✅ Saved {len(books)} books to '{filename}'")


# ─────────────────────────────────────────────
#  Display
# ─────────────────────────────────────────────
def display_books(books):
    if not books:
        print("\n⚠️  No books to display.")
        return
    print(f"\n{'='*65}")
    print(f"  {'#':<4} {'Title':<38} {'Price':<8} {'Rating'}")
    print(f"{'='*65}")
    for i, book in enumerate(books, 1):
        title = book["title"][:35] + "..." if len(book["title"]) > 35 else book["title"]
        stars = "⭐" * book["rating"]
        print(f"  {i:<4} {title:<38} {book['price']:<8} {stars}")
    print(f"{'='*65}")
    print(f"  Total: {len(books)} books")


# ─────────────────────────────────────────────
#  Input Helpers
# ─────────────────────────────────────────────
def get_int(prompt, min_val=1, max_val=50):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"  ⚠️  Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠️  Please enter a valid number.")


def get_float_optional(prompt):
    val = input(prompt).strip()
    if val == "":
        return None
    try:
        return float(val)
    except ValueError:
        print("  ⚠️  Invalid value, ignoring filter.")
        return None


# ─────────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   🕸️  Web Scraper — Books Data")
    print("   Synent Technologies Internship")
    print("   Source: books.toscrape.com")
    print("=" * 50)

    while True:
        print("\n📋 MENU")
        print("  1. Scrape Books")
        print("  2. Exit")

        choice = input("\nEnter choice (1-2): ").strip()

        if choice == "1":
            print("\n-- Scraping Settings --")
            pages      = get_int("  How many pages to scrape? (1-50): ", 1, 50)
            min_rating = get_int("  Minimum rating filter? (1-5): ", 1, 5)
            max_price  = get_float_optional("  Maximum price filter in £? (press Enter to skip): ")

            books = scrape_books(pages, min_rating, max_price)

            if not books:
                print("\n⚠️  No books found with given filters.")
                continue

            display_books(books)

            # Save options
            print("\n💾 Save Options:")
            print("  1. Save as JSON")
            print("  2. Save as CSV")
            print("  3. Save as Both")
            print("  4. Don't save")

            save_choice = input("\nEnter choice (1-4): ").strip()
            if save_choice == "1":
                save_json(books)
            elif save_choice == "2":
                save_csv(books)
            elif save_choice == "3":
                save_json(books)
                save_csv(books)
            else:
                print("  Data not saved.")

        elif choice == "2":
            print("\n👋 Goodbye! - Synent Technologies Internship\n")
            break

        else:
            print("\n⚠️  Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main()
