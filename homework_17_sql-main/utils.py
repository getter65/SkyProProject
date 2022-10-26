import psycopg2
from psycopg2 import Error


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


def sql_request(cursor):
    try:
        cursor.execute("""
        SELECT name, name_authors, price, description, address, is_published
        FROM ads
        JOIN addresses
        on ads.id_address=addresses.id_addr
        JOIN authors
        on ads.id_author=authors.id_aut
        """)
        data = cursor.fetchall()
        for d in data:
            print(','.join([str(i) for i in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def users(cursor):
    try:
        cursor.execute("""
        SELECT name_authors
        FROM authors
        """)
        for d in cursor.fetchall():
            print(','.join([str(k) for k in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def user_adverts(cursor, user):
    try:
        cursor.execute(f"""
        SELECT name, name_authors, price, description, address, is_published
        FROM ads
        JOIN addresses
        on ads.id_address=addresses.id_addr
        JOIN authors
        on ads.id_author=authors.id_aut
        WHERE authors.name_authors = '{user}'
        """)
        data = cursor.fetchall()
        if len(data) == 0:
            print('Такого имени не найдено. Введите имя как в списке ')
        else:
            for d in data:
                print(','.join([str(i) for i in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def between_price(cursor, min_price, max_price):
    try:
        cursor.execute(f"""
        SELECT name, name_authors, price, description, address, is_published
        FROM ads
        JOIN addresses
        on ads.id_address=addresses.id_addr
        JOIN authors
        on ads.id_author=authors.id_aut
        WHERE price BETWEEN {min_price} and {max_price}
        ORDER BY price ASC
        """)
        data = cursor.fetchall()
        if len(data) == 0:
            print('Такого товара не найдено. Попробуйте изменить параметры запроса')
        for d in data:
            print(','.join([str(i) for i in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def cities():
    print('Москва\nПушкин\nСанкт-Петербург')


def city_adverts(cursor, user_input_2):
    try:
        cursor.execute(f"""
        SELECT name, name_authors, price, description, address, is_published
        FROM ads
        JOIN addresses
        on ads.id_address=addresses.id_addr
        JOIN authors
        on ads.id_author=authors.id_aut
        WHERE address LIKE '{user_input_2}%'
        """)
        data = cursor.fetchall()
        if len(data) == 0:
            print('Такого города не найдено. Введите город как в списке ')
        else:
            for d in data:
                print(','.join([str(i) for i in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def user_price(cursor, user, min_price, max_price):
    try:
        cursor.execute(f"""
        SELECT name, name_authors, price, description, address, is_published
        FROM ads
        JOIN addresses
        on ads.id_address=addresses.id_addr
        JOIN authors
        on ads.id_author=authors.id_aut
        WHERE authors.name_authors = '{user}' and price BETWEEN {min_price} and {max_price} 
        """)
        data = cursor.fetchall()
        if len(data) == 0:
            print('Такого имени или товара не найдено. Попробуйте ввести имя как в списке или измените параметры '
                  'запроса ')
        else:
            for d in data:
                print(','.join([str(i) for i in d]))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
