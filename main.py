#############################################################################
from utils import func


def main():
    file_data = 'operations.json'

    # Загружаем из файла JSON результаты транзакции в список
    list_trans = func.load_data_file(file_data)

    # Формируем данные, необходимые для вывода на экран
    sort_list = func.filters_sorts(list_trans, ('state', 'EXECUTED'), 'date', rev=True, line_counter=5)

    # Вывод пяти последних успешных результатов транзакций
    for i in range(len(sort_list)):
        print(f"{func.date_format(sort_list[i]['date'])} {sort_list[i]['description']}")
        if sort_list[i].get('from') is None:
            print(f"{func.masks_numbers(sort_list[i]['to'])}")
        else:
            print(f"{func.masks_numbers(sort_list[i]['from'])} --> {func.masks_numbers(sort_list[i]['to'])}")
        print(f"{sort_list[i]['operationAmount']['amount']} {sort_list[i]['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    main()

#############################################################################
