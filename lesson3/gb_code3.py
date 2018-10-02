# for _ in range(10):
#     print('w')

# print(max(1,2,3,4,5,6))
# print(max('aaa', 'zz', key=len))

# full_name = input('Введите имя и фамилию:')


# def check_name(name):
#     if name == name.title():
#         print('Все ок')
#     else:
#         print('Формат неверный')
#
# def is_name_correct(name):
#     if name == name.title():
#         return True
#     else:
#         return False
#
# check_name(full_name)
#
# if is_name_correct(full_name):
#     print('Все ок')

# def my_summ(x, y):
#     return x + y
#     print(11111)
#
# result = my_summ(5, 5)
# print('Результат:',result)
# print(my_summ('qwe', 'rty'))

# def average(q, w, e, r, t, y):
#     sum = q + w + e + r + t + y
#     return sum / 6

# def average(*args):
#     summ = 0
#     for num in args:
#         summ += num
#     return summ / len(args)
#
# numbers = [1, 2, 3, 4, 5, 7, 8]
# result = average(*numbers)
# print(result)

# def person_card(name, surname='Guest', age=0):
#     print(name, surname, age)
#
# person_card('Ivan')
# person_card('Alice', 'Black')
# person_card('Alice', age=20, surname='Black')

# def person_card(**kwargs):
#     if kwargs.get('name'):
#         print('Имя', kwargs.get('name'))
#     print(kwargs)
#
# human = {'age': 20, 'money': 100.30}
# person_card(name='Ivan', age=20, surname='Black')
# person_card(name='Ivan', **human)

# def test(name, surname='Guest', *args, **kwargs):
#     print(name, surname, args, kwargs)
#
# test('Ivan', 'Ivanov', 1,2,3,4, age = 40 )

# z = 10
#
# server_ip = '1.1.1.1'
# server_port = '8080'
#
#
# def my_test(x):
#     zzz = 100
#     # global z - плохо!
#     z = 300
#     return z
#
# print(my_test(20))
# print(z)

# humans = ['Иван', 'Алиса']
# salaries = [100, 200, 300]
#
# result = zip(humans, salaries)
# print(list(result))
#
# result = zip(humans, salaries)
# print(dict(result))

# def my_data(x):
#     return (x + 10) / 3
#
# data = [-1, -2, -3, 4, 5, 6]
#
# result = []
# for value in data:
#     result.append(my_data(value))
#
# result = map(my_data, data)
# result = map(lambda x: (x + 10) / 3, data)
# print(list(result))
#
# result = filter(lambda x: x > 0, data)
# print(list(result))
#

# https://docs.python.org/3/library/os.path.html
# https://pythonworld.ru/moduli/modul-os.html

# import os
# print(os.path.exists('folder/1111123.txt'))
# print(os.path.exists('/home/sizov/1111123.txt'))

# file = open('123.txt', 'w')
# file.write('q\n')
# file.close()

# file = open('123.txt')
#
# # print(file.readlines())
# for line in file:
#     print(line.strip())
#     # print(line, end='')
#
# file.close()

with open('123.txt') as file:
    for line in file:
        print(line.strip())

# ДЗ от меня!!! 