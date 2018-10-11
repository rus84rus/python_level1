# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


# list = [2, -5, 8, 9, -25, 25, 4]
# list2 = []
# # print(list)
# for item in list:
#     item = item ** 0.5
#
#     # print(type(item), item, '\n')
#     if type(item) is float:
#         if item == int(item):
#             list2.append(int(item))
#         else:
#             continue
#     # elif type(item ** 0.5) is complex:
#     #     continue
#     else:
#         continue
# print(list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


# input='02.11.2013'
# date = {'day': '02', 'month': '11', 'year': '2013'}
# date['day'] = 'второе'
# date['month'] = 'ноября'
# date['year'] = '2013 года'
# print(date['day'] , date['month'], date['year'])
# list = []
# for value in date.values():
#     list.append(value)
#     print(value)
# print(date)
# print(list[0],list[1],list[2])

# создаем словари день, месяц, год

day_list_do_20 = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
                  'десятое',
                  'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                  'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое']
day_desytki=('двадцать','тридцать')
month_str = ['января', 'февраля', 'марта', 'апреля', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
             'декабрь']
days = {keys: value for keys, value in enumerate(day_list_do_20, 1)}
months = {keys: value for keys, value in enumerate(month_str, 1)}
years = [a for a in range(1, 2019)]
print(days)
#print(months)

# Вводим дату

date = input('Введите дату в формате дд.мм.гггг:')
date_list = date.split('.')

# day = days[input_list[0]]
if 0 < int(date_list[0]) <= 20:
    day = days[int(date_list[0])]
elif 21 <= int(date_list[0]) <= 29:
    day_split = list(date_list[0])
    day = str(day_desytki[1])+ ' ' + str(days[int(day_split[1])])
elif 30 <= int(date_list[0]) <= 31:
    day_split = list(date_list[0])
    day = str(day_desytki[1]) + ' ' + str(days[int(day_split[1])])

    # print(day)
else:
    print('введен не корректный день')
    day='XX'
if 0 < int(date_list[1]) <= 12:
    month = months[int(date_list[1])]
    # print(month)
else:
    print('введен не корректный месяц')
    month='XX'
if 0 < int(date_list[2]) <= 2018:
    year = date_list[2]
    # print(year)
else:
    print('еще не дожили до этого года')
    year='XX'


output = '{} {} {} года.'.format(day, month, year)
print(output)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
#
# from random import randint
# n=int(input('Введите желаемое количество элементов списка:'))
# list = [randint(-100, 100) for i in range(n)]
# print(list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# lst2 = set(lst)
# lst3 =[]
# # print(lst)
# print(list(lst2))
# # m=lst.count(2)
# # print(m)
# for i in lst:
#     count = lst.count(i)
#     if count == 1:
#         lst3.append(i)
#     # else:
#     #     continue
# print(lst3)