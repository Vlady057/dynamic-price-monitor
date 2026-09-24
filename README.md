
# Dynamic Price Monitor

A Python web automation project that uses Selenium to monitor product prices on [Quals.ua](https://quals.ua/) and stores price history in SQLite.

## Features

* Browser automation with `Selenium`
* Product search with Selenium
* HTML element extraction
* CSS selectors
* Explicit waits with `WebDriverWait`
* Product parsing from HTML `data-*` attributes
* SQLite database
* Price history tracking
* Price change detection
* Unit tests with `pytest`
* Modular project structure
* Demo SQLite database

## Extracted Data

The scraper extracts:

* Product title
* Price
* Product URL

The application stores product information and price history in SQLite.

Example database files are available in:

```text
data/example_prices.db
data/database_preview.md
```

## Project Structure

```text
dynamic-price-monitor/
├── data/
│   ├── example_prices.db
│   └── database_preview.md
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
├── README.md
├── requirements.txt
```

## How It Works

```text
Selenium
    ↓
Product Search
    ↓
Product Cards
    ↓
Parser
    ↓
Title / Price / URL
    ↓
SQLite
    ↓
Price Comparison
    ↓
Console Report
```

The scraper compares the current price with the previously stored price and detects:

```text
increased
decreased
unchanged
```

## Database

The project uses SQLite with two tables:

```text
products
    │
    └── price_history
```

`products` stores unique products.

`price_history` stores every observed price with a timestamp.

The working database is:

```text
data/prices.db
```

and is excluded from Git.

A smaller demo database is included for portfolio purposes:

```text
data/example_prices.db
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Vlady057/dynamic-price-monitor.git
cd dynamic-price-monitor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the price monitor:

```bash
python src/scraper.py
```

The application opens Chrome, searches for products, extracts their data, stores the results in SQLite, compares prices with previous checks, and displays the result in the console.

Example:

```text
The Beatles 1 (SHM-CD)

1800.00 → 1695.00 UAH
Change: -105.00 UAH (-5.83%)
Status: decreased
```

## Testing

Run all tests with:

```bash
pytest
```

Current test suite:

```text
12 passed
```

The tests cover:

* Price decrease
* Price increase
* Unchanged price
* Price status detection
* Price formatting
* Complete price change results

## Technologies

* Python 3.13
* Selenium
* SQLite
* CSS Selectors
* WebDriverWait
* pytest
* Git / GitHub
