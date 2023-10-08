import json
import os
from datetime import datetime


# def load_data_file_2(file_name):
#     """ Загружает данные из файла в формате JSON в список.
#         Возврашает список, удаляя пустые элементы
#         Если файла нет - возвращает None """
#
#     out_data = []
#     if os.path.exists(file_name):
#         with open(file_name, 'r', encoding='utf-8') as file:
#             for rec in json.load(file):
#                 if rec:
#                     out_data.append(rec)
#     else:
#         out_data = None
#     if not out_data:
#         return None
#     return out_data


def load_data_file(file_name):
    """ Загружает данные из файла в формате JSON в список.
        Возврашает список.
        Если файла нет - возвращает None """

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return None


# def date_in_sec(str_data):
#     """ Переводит строковое значение даты в абсолютное время в секундах """
#
#     lst_data = list(str_data)
#     ind = lst_data.index("T")
#     lst_data.pop(ind)
#     lst_data.insert(ind, " ")
#     # str_data = "".join(lst_data)
#     return "".join(lst_data)


def date_format(date_str):
    """ Приводит формат даты к требуемуму, убирая лишний символ 'T' """

    if 'T' in date_str:
        lst_data = list(date_str)
        ind = lst_data.index("T")
        lst_data.pop(ind)
        lst_data.insert(ind, " ")
        new_date = "".join(lst_data)
    else:
        new_date = date_str
    # Другой вариант реализации функции
    # new_date = ""
    # for char in date_str:
    #     if char != "T":
    #         new_date += char
    #     else:
    #         new_date += " "
    return datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')


def masks_numbers(code_str):
    """ Если строка содержит номер счета - то формат вывода **ХХХХ
        Если строка содержит номер банковской карты - то формат вывода ХХХХ ХХ** **** ХХХХ """

    code_lst = code_str.split()
    # Можно так:
    # code_str = "".join(list(filter(lambda x: x.isdigit(), code_lst)))
    # А можно так:
    code_str = code_lst[-1]
    if len(code_str) < 20:
        new_str = code_str[0:4] + " " + code_str[4:6] + "** **** " + code_str[-4:]
    else:
        new_str = "**" + code_str[-4:]
    return new_str


def filters_sorts(lst_data: list, fil_param: tuple, sort_param: str, rev=True, line_counter=None, ):
    """ Фильтрует список lst_data по параметру fil_param
        Сортирует список lst_data по параметру sort_param
        rev - направление сортировки: True - по убыванию, False - по возрастанию
        Возвращает отфильтрованый и отсортированый список
        line_counter - колличество возвращаемых элементов отсортированного списка """

    filter_lst = list(filter(lambda x: (x and x[fil_param[0]] == fil_param[1]), lst_data))
    new_lst = sorted(filter_lst, key=lambda date: date[sort_param], reverse=rev)
    if line_counter is not None and line_counter < len(new_lst):
        return new_lst[0: line_counter]
    return new_lst

# print(masks_numbers("Maestro 3928549031574026"))

# print(date_format("2019-12-08T22:46:21.935582"))

# fn = os.path.join('../', 'operations.json')
# open_lst = load_data_file(fn)

# print(open_dic)

# Ключи "data" в словаре переписываем в секунды абсолютного времени (для сортировки)
# for i in open_lst:
#     # print(i)
#     # i['date'] = date_in_sec(i['date'])
#     i['date'] = datetime.strptime(date_in_sec(i['date']), '%Y-%m-%d %H:%M:%S.%f').timestamp()
#     print(i)

# Вывод даты в требуемом формате, переводя из абсолютных секунд
# print(datetime.fromtimestamp(open_lst[0]['date']).strftime("%d.%m.%y"))
# print(date_in_sec(open_lst[0]['date']))
# print(datetime.strptime(date_in_sec(open_lst[0]['date']), '%Y-%m-%d %H:%M:%S.%f').timestamp())
