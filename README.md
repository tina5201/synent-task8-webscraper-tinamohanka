# 🕸️ Web Scraper — Books Data

**Synent Technologies – Python Development Internship**
**Task 8 – Advanced Level**

---

## 📌 Description

A command-line web scraper that extracts book data (title, price, rating, availability) from [books.toscrape.com](https://books.toscrape.com) — a free, legal practice website. Supports multi-page scraping, filtering, and saves output to both CSV and JSON formats.

---

## ✨ Features

- Scrape 1 to 50 pages of book data
- Extracts: Title, Price, Star Rating, Availability
- Filter by minimum rating (1–5 stars)
- Filter by maximum price (in £)
- Display results in a clean formatted table
- Save output as JSON, CSV, or both
- Error handling: timeouts, connection errors, HTTP errors
- Pagination support (auto-stops at last page)

---

## 🛠️ Tech Stack

- Python 3.x
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `json`, `csv` — built-in file saving

---

## ⚙️ Installation

Install required libraries:
```
pip install requests beautifulsoup4
```

---

## ▶️ How to Run

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/synent-task8-webscraper-yourname.git
   ```
2. Navigate to the folder:
   ```
   cd synent-task8-webscraper-yourname
   ```
3. Install dependencies:
   ```
   pip install requests beautifulsoup4
   ```
4. Run the script:
   ```
   python web_scraper.py
   ```

---

## 📸 Sample Output

```
==================================================
   🕸️  Web Scraper — Books Data
   Synent Technologies Internship
   Source: books.toscrape.com
==================================================

-- Scraping Settings --
  How many pages to scrape? (1-50): 2
  Minimum rating filter? (1-5): 3
  Maximum price filter in £? (press Enter to skip):

🔍 Scraping 2 page(s)...

  📄 Scraping page 1/2... ✅ 20 books found
  📄 Scraping page 2/2... ✅ 20 books found

=================================================================
  #    Title                                  Price    Rating
=================================================================
  1    A Light in the Attic                   £51.77   ⭐⭐⭐
  2    Tipping the Velvet                     £53.74   ⭐⭐⭐⭐⭐
=================================================================
  Total: 18 books
```

---

## 📁 File Structure

```
synent-task8-webscraper-yourname/
│
├── web_scraper.py    # Main program
├── books.json        # Auto-created after scraping
├── books.csv         # Auto-created after scraping
└── README.md
```

---

## 👤 Author

**Your Name**
Python Development Intern – Synent Technologies
