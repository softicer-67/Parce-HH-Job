from functions import get_data


def main():
    option = input('Введите слово для поиска вакансии: ')
    page = int(input('Колличество страниц: '))
    get_data(option, page)


if __name__ == '__main__':
    main()
