"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

PATH_CUS = './north_data/customers_data.csv'
PATH_EMPL = './north_data/employees_data.csv'
PATH_ORD = './north_data/orders_data.csv'

with open(PATH_EMPL, 'r', encoding="UTF-8") as file:
    """
    Получение данных из файла employees_data.csv 
    """
    employees_data = []
    reader_data = csv.DictReader(file, delimiter=',')
    for row in reader_data:
        employees_data.append(tuple(row))

with open(PATH_CUS, 'r', encoding="UTF-8") as file:
    """
    Получение данных из файла customers_data.csv
    """
    customers_data = []
    reader_data = csv.DictReader(file, delimiter=',')
    for row in reader_data:
        customers_data.append(tuple(row))

with open(PATH_ORD, 'r', encoding="UTF-8") as file:
    """
    Получение данных из файла orders_data.csv
    """
    orders_data = []
    reader_data = csv.DictReader(file, delimiter=',')
    for row in reader_data:
        orders_data.append(tuple(row))


conn = psycopg2.connect(host='localhost', database='north',
                        user='postgres', password='123456789')

cur = conn.cursor()

# Заполнение таблицы 'employees'
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees_data)

# Заполнение таблицы 'customers'
cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers_data)

# Заполнение таблицы 'orders'
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_data)
conn.commit()

cur.close()
conn.close()
