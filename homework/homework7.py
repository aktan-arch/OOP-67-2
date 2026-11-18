import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
''')
conn.commit()

def create_product(name, price, quantity):
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    print(f"Товар кошулду: {name}")

def read_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def update_product(id, price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, id))
    conn.commit()
    print(f"ID {id} товардын баасы өзгөрдү: {price}")

def delete_product(id):
    cursor.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    print(f"ID {id} товар өчүрүлдү")

create_product("Телефон", 50000, 10)
create_product("Ноутбук", 120000, 5)
create_product("Наушник", 2500, 20)

print("--- Бардык товарлар ---")
read_products()

update_product(1, 45000)
print("--- Жаңыргандан кийин ---")
read_products()

delete_product(3)
print("--- Өчүргөндөн кийин ---")
read_products()
