import json
import psycopg2
from psycopg2 import Error


def connection():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="northwind")
        connection.autocommit = True
        print('Connection Done')
        return connection
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return False


def create_sql_file():
    with open('suppliers.json') as file:
        list_dict = json.load(file)
    with open('set_change_northwind.sql', 'w', encoding='utf-8') as file:
        file.write("""
        CREATE TABLE IF NOT EXISTS suppliers (
             id_supplier INTEGER PRIMARY KEY NOT NULL,
             company_name VARCHAR(50) NOT NULL,
             contact_person VARCHAR(100),
             contact_person_position VARCHAR(30),
             country VARCHAR(30),
             state VARCHAR(20),
             zip_code VARCHAR(30),
             city VARCHAR(20),
             address VARCHAR(50),
             phone VARCHAR(50),
             fax VARCHAR(50),
             homepage VARCHAR(100)
        );
        """)

        file.write("""
            ALTER TABLE products
            ADD COLUMN fk_id_suppliers INTEGER REFERENCES suppliers(id_supplier);
        """)

        counter = 1
        for i in list_dict:
            id_supplier = counter
            company = i['company_name'].replace("'", "''")
            contact_person = (i['contact'].split(","))[0].replace("'", "''")
            contact_person_position = (i['contact'].split(","))[1].replace("'", "''")
            country = (i['address'].split(";"))[0]
            state = (i['address'].split(";"))[1]
            zip_code = (i['address'].split(";"))[2]
            city = (i['address'].split(";"))[3]
            address = (i['address'].split(";"))[4].replace("'", "''")
            phone = i['phone']
            fax = i['fax']
            homepage = i['homepage'].replace("'", "''")
            file.write(f"""
            INSERT INTO suppliers
            VAlUES ('{id_supplier}', '{company}', '{contact_person}', '{contact_person_position}', '{country}', '{state}', '{zip_code}', '{city}',
                  '{address}', '{phone}', '{fax}', '{homepage}');
            """)
            counter += 1

        counter = 1
        for i in list_dict:
            product = [v.replace("'", "''") for v in i['products']]
            if counter != len(list_dict):
                file.write(f"""
                UPDATE products SET fk_id_suppliers = {counter} WHERE product_name IN ('{"', '".join(product)}');
                """)
            else:
                file.write(f"""
                UPDATE products SET fk_id_suppliers = {counter} WHERE product_name IN ('{"', '".join(product)}')
                """)
            counter += 1
        print('SQL файл сформирован')


def send_data_to_db(cursor):
    with open('set_change_northwind.sql', 'r', encoding='utf-8') as file:
        data = file.read()
        redacted_data = data.split(';')
        for i in redacted_data:
            try:
                cursor.execute(i)
                print('Запросы отправлены в базу данных')
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)


def main():
    conn = connection()
    if conn:
        cursor = conn.cursor()
        create_sql_file()
        send_data_to_db(cursor)

        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
