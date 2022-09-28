from classes import HH


def main():
    while True:
        try:
            option = input('Введите слово для поиска вакансии: ')
            pages = int(input('Колличество вакансий: '))
            opt = HH(option, pages)
            opt.get_request()
        except ValueError:
            print('Ошибка ввода')
            continue
        while True:
            file = opt.load_file()
            res = []
            print(f'\n[1] - Вывод на экран:\n[2] - Сортировка по дате:\n[3] - Сохранить в json и выйти')
            user_input = input('Что посмотрим?: \n')
            if user_input == '1':
                print(opt.load_file())
            elif user_input == '2':
               res.append(file.rstrip('\n'))
               res = '\n'.join(res)
               print('\n'.join(sorted(res.split('\n'), reverse=True)))
            elif user_input == '3':
                print('Выход')
                break
            continue
        exit('Досвидания')


if __name__ == '__main__':
    main()
