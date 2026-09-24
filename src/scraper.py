from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from parser import parse_product
from database import (
    create_database,
    save_product,
    get_product_id,
    get_last_price,
    save_price
)
from price_monitor import check_price


URL = "https://quals.ua/"
SEARCH_QUERY = "The Beatles"


create_database()

driver = webdriver.Chrome()

try:
    driver.get(URL)

    wait = WebDriverWait(driver, 15)

    search_elements = driver.find_elements(
        By.CSS_SELECTOR,
        ".js-toggle-search"
    )

    search_elements[1].click()

    search_input = wait.until(
        lambda d: d.find_element(By.NAME, "search")
    )

    search_input.send_keys(SEARCH_QUERY)
    search_input.send_keys(Keys.ENTER)

    wait.until(
        lambda d: "product/search" in d.current_url
    )

    products = driver.find_elements(
        By.CSS_SELECTOR,
        "li.product"
    )

    print("=" * 50)
    print("PRICE MONITOR")
    print("=" * 50)
    print(f"PRODUCTS FOUND: {len(products)}")

    changes = []
    new_products = []

    for product in products:

        data = parse_product(product)

        save_product(
            data["title"],
            data["url"]
        )

        product_id = get_product_id(
            data["url"]
        )

        last_price = get_last_price(
            product_id
        )

        current_price = data["price"]

        if last_price is None:

            new_products.append({
                "title": data["title"],
                "price": current_price,
                "url": data["url"]
            })

        else:

            result = check_price(
                last_price,
                current_price
            )

            if result["status"] != "unchanged":

                changes.append({
                    "title": data["title"],
                    "old_price": last_price,
                    "new_price": current_price,
                    "difference": result["formatted_difference"],
                    "percentage": result["formatted_percentage"],
                    "status": result["status"],
                    "url": data["url"]
                })

        save_price(
            product_id,
            current_price
        )

    print("\n" + "=" * 50)
    print("PRICE CHANGES")
    print("=" * 50)

    if not changes:
        print("No price changes detected.")

    else:

        for item in changes:

            print(f"\n{item['title']}")
            print(
                f"{item['old_price']:.2f} → "
                f"{item['new_price']:.2f} UAH"
            )
            print(
                f"Change: {item['difference']} "
                f"({item['percentage']})"
            )
            print(f"Status: {item['status']}")
            print(f"URL: {item['url']}")

    print("\n" + "=" * 50)
    print("NEW PRODUCTS")
    print("=" * 50)

    if not new_products:
        print("No new products.")

    else:

        for item in new_products:

            print(f"\n{item['title']}")
            print(f"Price: {item['price']:.2f} UAH")
            print(f"URL: {item['url']}")

    print("\n" + "=" * 50)
    print(
        f"SUMMARY: {len(changes)} price changes, "
        f"{len(new_products)} new products"
    )
    print("=" * 50)

finally:
    driver.quit()