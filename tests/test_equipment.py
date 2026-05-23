import sys
import os
import pytest
import sqlite3
import equipment_manager

TEST_DB = 'test_equipment.db'

# Перед началом тестов заменяем имя базы данных на тестовую
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Перед тестами
    equipment_manager.DATABASE = TEST_DB
    # Создаем таблицу
    equipment_manager.create_table()
    yield
    # После тестов - удаляем тестовую базу данных
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_add_and_update_and_delete_equipment():
    # добавление оборудования
    equipment_manager.add_equipment(
        type_='Laptop',
        brand='Dell',
        model='XPS 13',
        serial_number='SN123456',
        location='Office',
        status='Active',
        purchase_date='2023-01-15',
        warranty_period=24,
        responsible_person='John Doe'
    )

    # Проверка, что запись есть
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Equipment WHERE SerialNumber=?", ('SN123456',))
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    equipment_id = row[0]

    # Обновление записи
    equipment_manager.update_equipment(equipment_id, Status='Inactive')

    # Проверка обновления
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT Status FROM Equipment WHERE ID=?", (equipment_id,))
    status_row = cursor.fetchone()
    conn.close()

    assert status_row[0] == 'Inactive'

    # Удаление оборудования
    equipment_manager.delete_equipment(equipment_id)

    # Проверка удаления
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Equipment WHERE ID=?", (equipment_id,))
    row = cursor.fetchone()
    conn.close()

