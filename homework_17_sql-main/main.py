from utils import *


def main():
    conn = connection()
    if conn:
        cursor = conn.cursor()
        while True:
            print(
                'Выбрать запрос:\n1. Вывести все объявления\n2. Вывести объявления пользователя\n3. '
                'Вывести объявления в указанном диапазоне цен и отсортировать данные в порядке возрастания цены\n4. '
                'Выести объявления для конкретного города\n5. Вывести информацию для определенного пользователя и цены')
            user_input = input('Введите номер запроса: ')
            if user_input.isdigit() and 0 < int(user_input) < 6:
                if int(user_input) == 1:
                    sql_request(cursor)
                elif int(user_input) == 2:
                    print('На доске представлены объявления следующих пользователей:')
                    users(cursor)
                    user_input_2 = input('Введите имя пользователя: ')
                    user_adverts(cursor, user_input_2)
                elif int(user_input) == 3:
                    user_input_1 = input('Введите минимальную стоимость товара: ')
                    user_input_2 = input('Введите максимальную стоимость товара: ')
                    if user_input_1.isdigit() and user_input_2.isdigit():
                        between_price(cursor, user_input_1, user_input_2)
                    else:
                        print('Введите цифровое значение больше нуля!!!')
                elif int(user_input) == 4:
                    print('На доске представлены объявления следующих городов:')
                    cities()
                    user_input_2 = input('Введите город объявления которого вы хотите увидеть: ')
                    city_adverts(cursor, user_input_2)
                elif int(user_input) == 5:
                    print('На доске представлены объявления следующих пользователей:')
                    users(cursor)
                    user_input_1 = input('Введите пользователя объявления которого вы хотите увидеть: ')
                    user_input_2 = input(f'Введите минимальную стоимость товара пользователя {user_input_1}: ')
                    user_input_3 = input(f'Введите максимальную стоимость товара пользователя {user_input_1}: ')
                    if user_input_2.isdigit() and user_input_3.isdigit():
                        user_price(cursor, user_input_1, user_input_2, user_input_3)
                        break
                    else:
                        print('Вы ввели неверные запросы\nВведите имя из списка и цифровое значение больше нуля!!!')
            else:
                print('Введите запрос в пределе заданного диапазона!!!')


if __name__ == '__main__':
    main()
