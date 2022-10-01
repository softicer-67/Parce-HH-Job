from utils import *


def main() -> None:
    data = ''
    while True:
        user_input = input(f'\n[1] - Парсить hh.ru (max = 100)\n[2] - Вывести все\n'
                           f'[3] - Сортировать по дате\n[4] - Вывести 10 последних\n\n'
                           f'[5] - Парсить superjob.ru\n[6] - Вывести все\n[7] - Сортировать по дате\n'
                           f'[8] - Вывести 10 последних\n\n[9] - Сохранить в json и выйти\n')

        match user_input:
            case '1':
                option = input('Введите слово для поиска вакансии hh: ')
                pages = int(input('Колличество вакансий: '))
                if pages > 100:
                    print('максимальное число 100')
                    continue
                get_hh_vacs(option, int(pages))
                data = output_hh()
            case '2':
                print('\n'.join(data))
            case '3':
                res = '\n'.join(data)
                print('\n'.join(sorted(res.split('\n'), reverse=True)))
            case '4':
                res = '\n'.join(data)
                res = '\n'.join(set(str(res).split('\n')))
                print('\n'.join(sorted(res.split('\n')[:10], reverse=True)))
            case '5':
                option = input('Введите слово для поиска вакансии sj: ')
                pages = int(input('Колличество вакансий: '))
                get_sj_vacs(option, int(pages))
                data = output_sj()
            case '6':
                print('\n'.join(data))
            case '7':
                res = '\n'.join(data)
                res = '\n'.join(set(str(res).split('\n')))
                print('\n'.join(sorted(res.split('\n'), reverse=True)))
            case '8':
                res = '\n'.join(data)
                res = '\n'.join(set(str(res).split('\n')))
                print('\n'.join(sorted(res.split('\n')[:10], reverse=True)))
            case _:
                break


if __name__ == '__main__':
    main()
