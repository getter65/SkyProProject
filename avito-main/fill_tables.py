import psycopg2
from psycopg2 import Error
import csv


def connection():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="avito")
        connection.autocommit = True
        print('Connection Done')
        return connection
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return False


def author_table_filling():
    list_names = []
    with open('name.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0], row[1]
            list_names.append(s)
            data = ",".join(map(str, list_names))
        return data


def address_table_filling():
    list_addresses = []
    with open('address.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0], row[1]
            list_addresses.append(s)
            data = ",".join(map(str, list_addresses))
        return data


def ads_table_filling():
    list_ads = []
    with open('new_ads.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            list_ads.append(s)
            data = ",".join(map(str, list_ads))
        return data


def fill_authors_table(cursor, data):
    req = f"""
        INSERT INTO
            authors (name_authors, id_aut)
        VALUES
            {data}
        """
    try:
        cursor.execute(req)
        print(f'Таблица создана')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def fill_address_table(cursor, data):
    req = f"""
        INSERT INTO
            addresses (address, id_addr)
        VALUES
            {data}
        """
    try:
        cursor.execute(req)
        print(f'Таблица создана')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def fill_ads_table(cursor, data):
    req = f"""
        INSERT INTO
            ads (Id, name, id_author, price, description, id_address, is_published)
        VALUES
            {data}
        """
    try:
        cursor.execute(req)
        print(f'Таблица создана')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)



def main():
    conn = connection()
    if conn:
        cursor = conn.cursor()
        # data = author_table_filling()
        # fill_authors_table(cursor, data)
        # data_1 = address_table_filling()
        # fill_address_table(cursor, data_1)
        data_2 = ads_table_filling()
        fill_ads_table(cursor, data_2)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
