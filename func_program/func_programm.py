def filterer(data: list, val: str) -> list:
    return [i for i in data if val in i]


def maper(data: list, val: str) -> list:
    return [i.split()[int(val)] for i in data]


def uniquer(data: list) -> list:
    return list(set(data))


def sorter(data: list, value: str) -> list:
    if value == 'asc':
        return sorted(data, reverse=False)
    elif value == 'desc':
        return sorted(data, reverse=True)


def limiter(data: list, val: str) -> list:
    return [data[i] for i in range(int(val))]


def func_data(data: list, com: str, val: str) -> list:
    if com == 'filter':
        return filterer(data, val)
    elif com == 'map' and val.isdigit():
        return maper(data, val)
    elif com == 'unique' and val == '-':
        return uniquer(data)
    elif com == 'sort' and val in ['asc', 'desc']:
        return sorter(data, val)
    elif com == 'limit' and val.isdigit():
        return limiter(data, val)
    else:
        return []


def main():
    while True:
        with open('apache_logs.txt') as file:
            data = file.readlines()
        user_input = input("1.Введите команду\n2.Введите exit для выхода\n>>> ")
        commands = user_input.split(' | ')
        for command in commands:
            command_list = command.split()
            if len(command_list) != 2:
                print('Не верно введенная команда\n')
                continue
            data = func_data(data, command_list[0], command_list[1])
            if not data:
                print('Не верно введенная команда\n')
                continue
            elif user_input == 'exit':
                quit()
        for line in data:
            print(line)


if __name__ == "__main__":
    main()
