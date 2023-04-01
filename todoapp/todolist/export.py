import sqlite3
from openpyxl import Workbook

def export_to_excel():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Получаем список столбцов таблицы
    cursor.execute("PRAGMA table_info(table_name)")
    table_columns = [col[1] for col in cursor.fetchall()]

    # Получаем данные из таблицы
    cursor.execute("SELECT * FROM todolist_todo")
    table_data = cursor.fetchall()

    # Создаем новый файл Excel и записываем данные в него
    wb = Workbook()
    ws = wb.active
    ws.append(table_columns)
    for row in table_data:
        ws.append(row)

    wb.save('exported_data.xlsx')