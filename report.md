# Project Report - Web Scraper

**Internship:** Synent Technologies - Python Development  
**Task:** Task 8 - Advanced Level  
**Author:** Tina Kumari Mohanka  
**Date:** June 2026  

---

## Objective

To build a web scraper that extracts book data (title, price, rating, availability) from a live website, with filtering options and export to CSV and JSON formats.

---

## Tools Used

- Python 3
- `requests` library - sending HTTP requests
- `beautifulsoup4` library - parsing HTML content
- `json` module - saving data as JSON
- `csv` module - saving data as CSV
- VS Code - code editor
- GitHub - version control
- Website used: [books.toscrape.com](https://books.toscrape.com) - free, legal practice site

---

## Steps Performed

1. Sent HTTP GET request to `books.toscrape.com` using `requests`
2. Parsed HTML response using `BeautifulSoup`
3. Extracted book details - title, price, star rating, availability
4. Implemented pagination - scrape 1 to 50 pages
5. Added filter by minimum star rating (1-5)
6. Added filter by maximum price in £
7. Displayed scraped data in a clean formatted table
8. Added option to save output as JSON, CSV, or both
9. Added error handling - connection errors, timeouts, HTTP errors
10. Tested with multiple page counts and filter combinations

---

## Output

- Book data successfully scraped from multiple pages
- Filters working correctly - rating and price filters applied
- Data exported to `books.json` and `books.csv`
- Error messages displayed clearly for network issues

---

## What I Learned

- How web scraping works - HTTP requests and HTML parsing
- Using `BeautifulSoup` to navigate and extract HTML elements
- Handling pagination in web scraping
- Exporting structured data to CSV and JSON
- Writing robust error handling for network-dependent programs
