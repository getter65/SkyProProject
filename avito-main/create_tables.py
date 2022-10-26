import psycopg2
from psycopg2 import Error


def create_tables(reg):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="avito")
        cursor = connection.cursor()
        cursor.execute(reg)
        print(f'Таблица создана')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            connection.commit()
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


request = """
    CREATE TABLE IF NOT EXISTS authors (
    name_authors VARCHAR(30),
    id_aut SERIAL PRIMARY KEY
    )
    """

request_1 = """
    CREATE TABLE IF NOT EXISTS addresses (
    address VARCHAR(80),
    id_addr SERIAL PRIMARY KEY
    )
    """

request_2 = """
       CREATE TABLE IF NOT EXISTS ads (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        id_author INTEGER NOT NULL,
        price NUMERIC NOT NULL,
        description TEXT NOT NULL,
        id_address INT NOT NULL,
        is_published VARCHAR(10) NOT NULL,
        FOREIGN KEY (id_author) REFERENCES authors (id_aut),
        FOREIGN KEY (id_address) REFERENCES addresses (id_addr)
       )
       """

def main():
    create_tables(request)
    # create_tables(request_1)
    # create_tables(request_2)


if __name__ == '__main__':
    main()
