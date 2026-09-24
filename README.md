
# Dynamic Price Monitor

A Python-based price monitoring tool that uses Selenium to search products on a real e-commerce website, stores product and price history in SQLite, detects price changes, and validates the business logic with pytest.

## Features

* Automated browser-based product search with Selenium
* Dynamic extraction of product title, price, and URL
* SQLite database for product and price history
* Detection of price increases, decreases, and unchanged prices
* Calculation of absolute and percentage price changes
* Detection of newly discovered products
* Automated tests with pytest
* Separation of scraping, parsing, database, and business logic

## Tech Stack

* Python 3.13+
* Selenium
* SQLite
* pytest
* Quals.ua

## Project Structure

```text
dynamic-price-monitor/
├── data/
│   └── prices.db
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── parser.py
│   ├── price_monitor.py
│   └── scraper.py
├── tests/
│   └── test_price_change.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Architecture

```text
                    Selenium
                       │
                       ▼
                  Quals.ua
                       │
                Product Search
                       │
                       ▼
                  scraper.py
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        parser.py           database.py
             │                   │
             │             ┌─────┴─────┐
             │             ▼           ▼
             │        products    price_history
             │                         │
             └────────────┬────────────┘
                          ▼
                  price_monitor.py
                          │
                ┌─────────┼─────────┐
                ▼         ▼         ▼
             increase   decrease  unchanged
                          │
                          ▼
                    Console Report

                  pytest
                     │
                     ▼
             Business Logic Tests
```

## Database Design

The application uses SQLite with two main tables.

### `products`

Stores unique product information:

| Field     | Description         |
| --------- | ------------------- |
| `id`    | Primary key         |
| `title` | Product name        |
| `url`   | Product URL, unique |

### `price_history`

Stores every observed price:

| Field          | Description         |
| -------------- | ------------------- |
| `id`         | Primary key         |
| `product_id` | Related product     |
| `price`      | Observed price      |
| `checked_at` | Time of price check |

This structure allows the application to preserve price history instead of overwriting the previous price.

## How It Works

### 1. Selenium opens the website

The scraper starts Chrome through Selenium and opens the target website.

### 2. Product search

The application performs a search for:

```text
The Beatles
```

### 3. Product extraction

The scraper finds product cards dynamically and passes each Selenium element to `parser.py`.

The parser extracts:

```text
title
price
url
```

### 4. Database storage

The product is saved to SQLite.

The application then retrieves the previous recorded price and compares it with the current price.

### 5. Price monitoring

`price_monitor.py` calculates:

```text
absolute difference
percentage difference
price status
```

Possible statuses:

```text
increased
decreased
unchanged
```

### 6. Console report

The application displays price changes and newly discovered products.

## Example Output

```text
==================================================
PRICE MONITOR
==================================================
PRODUCTS FOUND: 5

==================================================
PRICE CHANGES
==================================================
No price changes detected.

==================================================
NEW PRODUCTS
==================================================
No new products.

==================================================
SUMMARY: 0 price changes, 0 new products
==================================================
```

Example of a detected price decrease:

```text
The Beatles 1 (SHM-CD)
1800.00 → 1695.00 UAH
Change: -105.00 UAH (-5.83%)
Status: decreased
```

## Installation

Clone the repository:

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd dynamic-price-monitor
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Application

From the project root:

```powershell
python src/scraper.py
```

The application will:

1. Open Quals.ua
2. Search for products
3. Extract product information
4. Save products and prices to SQLite
5. Compare the current price with the previous price
6. Display the monitoring report

Selenium Manager is used to manage the browser driver with current Selenium versions.

## Run Tests

Run:

```powershell
pytest
```

Current result:

```text
12 passed in 0.05s
```

The test suite covers:

* price decrease
* price increase
* unchanged price
* price status detection
* price formatting
* complete `check_price()` results

## Code Responsibilities

### `scraper.py`

Main application workflow.

Responsible for:

* opening the website
* performing the search
* locating products
* calling the parser
* interacting with the database
* checking price changes
* displaying results

### `parser.py`

Responsible for extracting structured data from Selenium elements:

```text
title
price
url
```

### `database.py`

Responsible for SQLite operations:

* database creation
* saving products
* finding products
* retrieving previous prices
* saving price history

### `price_monitor.py`

Contains the application's business logic:

* calculating price differences
* calculating percentage changes
* determining price status
* formatting monitoring results

### `tests/test_price_change.py`

Contains automated pytest tests for the price-monitoring logic.

## QA / Automation Skills Demonstrated

This project demonstrates practical experience with:

* Selenium WebDriver
* UI automation
* CSS selectors
* explicit waits
* HTML `data-*` attributes
* web scraping
* HTTP/web concepts
* SQLite
* SQL queries
* Python modules and packages
* pytest
* test cases and assertions
* business-logic testing
* database persistence
* separation of responsibilities
* debugging import/package issues
* Git/GitHub project organization

## Project Limitations

This is a portfolio and learning project using a real public e-commerce website.

The scraper does not attempt to bypass:

* CAPTCHA
* Cloudflare
* authentication
* anti-bot protection

Website HTML structures can change, so Selenium selectors may require maintenance if the target website changes its frontend.

## Future Improvements

Possible extensions:

* configurable search queries
* monitoring multiple products
* scheduled price checks
* email notifications
* Telegram notifications
* logging
* configuration through environment variables
* additional integration tests
* support for multiple websites
* price-history visualization
* web dashboard

## Author

Vladimir

Junior QA Engineer / Junior QA Automation portfolio project

Focus areas:

```text
Python
Selenium
Web Scraping
SQL
SQLite
pytest
Test Automation
```
