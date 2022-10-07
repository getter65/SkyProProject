from utils import hh_data, sj_data, combine, load_vacancy


def main():
    jobs_at_hh = hh_data()
    load_vacancy(jobs_at_hh)
    jobs_at_sj = sj_data()
    load_vacancy(jobs_at_sj)
    combined_list = combine()
    print(combined_list)
    print(type(combined_list))

    while True:
        user_input = input('Выберите действие:\n1. Сформировать список 10 случайных вакансий с HH\n2. Сформировать список вакансий с '
            'SJ\n3. Вывести все вакансии\n4. Вывести 5 вакансий с наибольшей зарплатой\n5. Выход\nВвод: ')
        if user_input == '1':
            for i in range(10):
                print(i, combined_list[i])
        elif user_input == '3':
            print(combined_list)
        elif user_input == '4':
            pass
        elif user_input == '5':
            quit()


if __name__ == '__main__':
    main()






