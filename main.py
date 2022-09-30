from utils import *


def main() -> None:
    while True:
        user_input = input(f'\n[1] - Парсить hh.ru\n[2] - Вывести все\n'
                           f'[3] - Сортировать по дате\n[4] - Вывести 10 последних\n\n'
                           f'[5] - Парсить superjob.ru\n[6] - Вывести все\n[7] - Вывести 10 последних\n\n'
                           f'[8] - Сохранить в json и выйти\n')
        match user_input:
            case '1':
                option = input('Введите слово для поиска вакансии: ')
                pages = int(input('Колличество вакансий: '))
                get_hh_vacs(option, int(pages))
            case '2':
                data = output_hh()
                print('\n'.join(data))
            case '3':
                data = output_hh()
                res = '\n'.join(data)
                print('\n'.join(sorted(res.split('\n'), reverse=True)))
                print('-' * 150)
            case '4':
                data = output_hh()
                res = '\n'.join(data)
                res = '\n'.join(set(str(res).split('\n')))
                print('\n'.join(sorted(res.split('\n')[:10], reverse=True)))
                print('-' * 150)
            case '5':
                option = input('Введите слово для поиска вакансии: ')
                pages = int(input('Колличество вакансий: '))
                get_sj_vacs(option, int(pages))
            case '6':
                data1 = output_sj()
                print('\n'.join(data1))
            case '7':
                data1 = output_sj()
                res = '\n'.join(data1)
                res = '\n'.join(set(str(res).split('\n')))
                print('\n'.join(sorted(res.split('\n')[:10], reverse=True)))
                print('-' * 150)
            case _:
                break


if __name__ == '__main__':
    main()
