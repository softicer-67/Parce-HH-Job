from typing import List

from classes import HH, Superjob


def main() -> None:
    while True:
        try:
            res = []
            res_2 = []
            print(f'\n[1] - Парсить hh.ru:\n[2] - Вывод на экран:\n'
                  f'[3] - Сортировка по дате:\n\n[4] - Парсить superjob.ru:\n'
                  f'[5] - Вывод на экран:\n\n[6] - Сохранить в json и выйти')
            user_input = input('\nЧто посмотрим?: \n')
            if user_input == '1':
                option = input('Введите слово для поиска вакансии: ')
                pages = int(input('Колличество вакансий: '))
                cls_1 = HH(option, pages)
                cls_1.get_request()
            elif user_input == '2':
                file = cls_1.load_file()
                print(file)
            elif user_input == '3':
               res.append(file.rstrip('\n'))
               res = '\n'.join(res)
               print('\n'.join(sorted(res.split('\n'), reverse=True)))

            elif user_input == '4':
                option = input('Введите слово для поиска вакансии: ')
                pages = int(input('Колличество вакансий: \n'))
                cls_2 = Superjob(option, pages)
                file = cls_2.get_request()
            elif user_input == '5':
                for k, v in file.items():
                    try:
                        res_2.append(
                            f"{v['title']} от {v['salary']} руб {v['url']} {v['desc'][:50]}...")
                    except TypeError:
                        continue
                res_2 = str(res_2).rstrip('\n')
                print('\n'.join(res_2.split(', ')).replace('[', '').replace(']', '').replace("'", ''))

            elif user_input == '6':
                print('Выход')
                break
        except Exception:
            continue
    exit('Досвидания')


if __name__ == '__main__':
    main()
