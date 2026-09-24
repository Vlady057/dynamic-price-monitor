import sqlite3


DB_PATH = "data/prices.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    connection.commit()
    connection.close()


def save_product(title, url):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO products (title, url)
        VALUES (?, ?)
        """,
        (title, url)
    )

    connection.commit()
    connection.close()


def get_product_id(url):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM products WHERE url = ?",
        (url,)
    )

    result = cursor.fetchone()

    connection.close()

    return result[0] if result else None


def get_last_price(product_id):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT price
        FROM price_history
        WHERE product_id = ?
        ORDER BY checked_at DESC
        LIMIT 1
        """,
        (product_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result[0] if result else None


def save_price(product_id, price):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO price_history (product_id, price)
        VALUES (?, ?)
        """,
        (product_id, price)
    )

    connection.commit()
    connection.close()


def get_products():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            products.id,
            products.title,
            price_history.price,
            products.url,
            price_history.checked_at
        FROM products
        JOIN price_history
            ON products.id = price_history.product_id
        ORDER BY products.id, price_history.checked_at
    """)

    products = cursor.fetchall()

    connection.close()

    return products