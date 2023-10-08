#############################################################################
from utils import func


def main():
    file_data = 'operations.json'

    # Загружаем из файла JSON результаты транзакции в список
    list_trans = func.load_data_file(file_data)

    # Формируем данные, необходимые для вывода на экран
    sort_list = func.filters_sorts(list_trans, ('state', 'EXECUTED'), 'date', rev=True, line_counter=5)



    # Убираем из списка транзакций операци со статусом перевода 'CANCELED'
    # filter_lst = list(filter(lambda x : (x and x['state'] == 'EXECUTED'), list_trans))

    # Производим сортировку по дате
    # new_lst = sorted(filter_lst, key=lambda date: date['date'], reverse=True)

    # func.date_in_sec(list_trans)

    for i in range(len(sort_list)):
        # list_trans[i]['date'] = func.date_in_sec(list_trans[i]['date'])
        print(sort_list[i])


if __name__ == '__main__':
    main()

#############################################################################
