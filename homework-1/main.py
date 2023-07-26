"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

# создаем соединение
conn = psycopg2.connect(
    dbname='north',
    user='postgres',
    password='renuar',
    host='localhost'
)

# создаем курсор
cur = conn.cursor()

# открываем CSV-файл с данными
with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок
    for row in reader:
        # вставляем данные в таблицу
        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )

# для таблицы customers
with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок
    for row in reader:
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s)",
            row
        )

# для таблицы orders
with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок
    for row in reader:
        cur.execute(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
            row
        )


# сохраняем изменения
conn.commit()

# закрываем соединение
cur.close()
conn.close()
