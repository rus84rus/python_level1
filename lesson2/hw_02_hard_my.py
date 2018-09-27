# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

# str = 'y=-2x+12'
# x=2
# split1 = str.split('=')
# split2 = str.split('+')
# print(split1, split2)
# b = float(split2[1])
# print(b)
# k = split2[0]
# k_temp = k.replace('y', ' ')
# k_temp = k_temp.replace('=', ' ')
# k_temp= k_temp.replace('x','')
# k=float(k_temp)
# print(k)
# y=k*x+b
# print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)


# day_list_do_20 = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
#                   'десятое',
#                   'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
#                   'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое']
# day_list_30 = 'тридцатое'
# day_desytki = ('двадцать', 'тридцать')
# month_str = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
#              'декабря']
# days = {keys: value for keys, value in enumerate(day_list_do_20, 1)}
# months = {keys: value for keys, value in enumerate(month_str, 1)}
# years = [a for a in range(1, 9999)]
# month_31 = ['02', '04', '06', '09', '11']
# # print(days)
# # print(months)
#
# # Вводим дату
# date_ok = True
# date = input('Введите дату в формате дд.мм.гггг:')
# if len(date) != 10:
#     date_ok = False
#     print('Введите дату в нужном формате')
# date_list = date.split('.')
# if len(date_list) != 3:
#     date_ok = False
#     print('Введите дату в нужном формате')
# else:
#     temp_day, temp_month, temp_year = date_list[0], date_list[1], date_list[2]
#     # print(temp_day, temp_month, temp_year)
#     # print(type(temp_day), type(temp_month), type(temp_year))
# if date_ok:
#     if len(temp_day) != 2 or not temp_day.isdigit():
#         date_ok = False
#         print('Введен некорректный день')
#     if len(temp_month) != 2 or not temp_month.isdigit():
#         date_ok = False
#         print('Введен некорректный месяц')
#     if len(temp_year) != 4 or not temp_year.isdigit():
#         date_ok = False
#         print('Введен некорректный год')
# if date_ok and date_list[0] == '31' and date_list[1] in month_31:
#     date_ok = False
#     print('В этом месяце нет столько дней')
# if date_ok and date_list[1] == '02' and int(date_list[0]) > 28:
#     date_ok = False
#     print('В феврале нет столько дней')
# if date_ok:
#     if 0 < int(date_list[0]) <= 20:
#         day = days[int(date_list[0])]
#     elif 21 <= int(date_list[0]) <= 29:
#         day_split = list(date_list[0])
#         day = str(day_desytki[0]) + ' ' + str(days[int(day_split[1])])
#     elif int(date_list[0]) == 30:
#         day = day_list_30
#     elif int(date_list[0]) == 31:
#         day_split = list(date_list[0])
#         day = str(day_desytki[1]) + ' ' + str(days[int(day_split[1])])
#     else:
#         print('введен некорректный день')
#         day = 'XX'
#     if 0 < int(date_list[1]) <= 12:
#         month = months[int(date_list[1])]
#     else:
#         print('введен некорректный месяц')
#         month = 'XX'
#     if 0 < int(date_list[2]) <= 9999:
#         year = int(date_list[2])
#     else:
#         print('введен некорректный год')
#         year = 'XXXX'
#     # else:
#     #     print('Введена некоректная дата')
#
#     output = '{} {} {} года.'.format(day, month, year)
#     print(output)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

ap = 12
count=0
while cout==ap:


    print(sk_ap)


