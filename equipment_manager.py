import sqlite3

# Имя файла базы данных
DATABASE = 'equipment.db'

# Функция для получения соединения с базой данных
def get_connection():
    return sqlite3.connect(DATABASE)

# Функция для создания таблицы, если она еще не существует
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Equipment (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Type VARCHAR(50),
        Brand VARCHAR(50),
        Model VARCHAR(50),
        SerialNumber VARCHAR(100) UNIQUE,
        Location VARCHAR(50),
        Status VARCHAR(20),
        PurchaseDate DATE,
        WarrantyPeriod INTEGER,
        ResponsiblePerson VARCHAR(50)
    )
    ''')
    conn.commit()
    conn.close()
    print("Таблица успешно создана или уже существует.")

# Функция для добавления нового оборудования
def add_equipment(type_, brand, model, serial_number, location, status, purchase_date, warranty_period, responsible_person):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Equipment (Type, Brand, Model, SerialNumber, Location, Status, PurchaseDate, WarrantyPeriod, ResponsiblePerson)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (type_, brand, model, serial_number, location, status, purchase_date, warranty_period, responsible_person))
        conn.commit()
        print("Запись успешно добавлена.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка при добавлении: {e}")
    finally:
        conn.close()
def update_equipment(id, **kwargs):
    conn = get_connection()
    cursor = conn.cursor()
    fields = []
    values = []
    for key, value in kwargs.items():
        fields.append(f"{key} = ?")
        values.append(value)
    values.append(id)
    sql = f"UPDATE Equipment SET {', '.join(fields)} WHERE ID = ?"
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print(f"Объект с ID={id} обновлен.")
def delete_equipment(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Equipment WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Объект с ID={id} удален.")
