from selenium.webdriver.common.by import By


def parse_product(product):
    title = product.get_attribute("data-item_name")
    price = product.get_attribute("data-price")

    link = product.find_element(
        By.CSS_SELECTOR,
        "a.woocommerce-LoopProduct-link"
    )

    url = link.get_attribute("href")

    return {
        "title": title,
        "price": float(price),
        "url": url
    }