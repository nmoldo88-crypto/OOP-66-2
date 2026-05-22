


import sqlite3


# ====================== Подключение к базе данных ======================
def get_connection():
    """Подключается к базе данных store.db"""
    conn = sqlite3.connect('store.db')
    return conn


# ====================== Создание таблицы ======================
def create_table():
    """Создаёт таблицу products, если её ещё нет"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS products
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       name
                       TEXT
                       NOT
                       NULL,
                       price
                       REAL
                       NOT
                       NULL,
                       quantity
                       INTEGER
                       NOT
                       NULL
                   )
                   ''')

    conn.commit()
    conn.close()
    print("✅ Таблица 'products' успешно создана или уже существует.")


# ====================== CRUD ОПЕРАЦИИ ======================

# 1. CREATE — Добавление товара
def create_product(name, price, quantity):
    """Добавляет новый товар в базу"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO products (name, price, quantity)
                   VALUES (?, ?, ?)
                   ''', (name, price, quantity))

    conn.commit()
    conn.close()
    print(f"✅ Товар '{name}' успешно добавлен!")


# 2. READ — Показать все товары
def read_products():
    """Выводит все товары из базы"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    if not products:
        print("📭 В базе пока нет товаров.")
        return

    print("\n📋 Список товаров:")
    print("-" * 60)
    print(f"{'ID':<5} {'Название':<25} {'Цена':<10} {'Количество':<10}")
    print("-" * 60)

    for product in products:
        print(f"{product[0]:<5} {product[1]:<25} {product[2]:<10} {product[3]:<10}")


# 3. UPDATE — Обновление цены товара
def update_product(product_id, new_price):
    """Обновляет цену товара по ID"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   UPDATE products
                   SET price = ?
                   WHERE id = ?
                   ''', (new_price, product_id))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        print(f"✅ Цена товара с ID {product_id} обновлена на {new_price}")
    else:
        print(f"❌ Товар с ID {product_id} не найден.")


# 4. DELETE — Удаление товара
def delete_product(product_id):
    """Удаляет товар по ID"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        print(f"🗑️ Товар с ID {product_id} успешно удалён.")
    else:
        print(f"❌ Товар с ID {product_id} не найден.")


# ====================== ТЕСТ ======================
if __name__ == "__main__":
    create_table()  # Создаём таблицу при первом запуске

    # Добавляем тестовые товары
    create_product("Ноутбук Lenovo", 75000, 5)
    create_product("Мышь Logitech", 1500, 20)
    create_product("Клавиатура", 3200, 10)

    # Показываем все товары
    read_products()

    # Обновляем цену
    update_product(1, 72000)

    # Удаляем товар
    # delete_product(2)

    # Показываем результат после изменений
    read_products()
