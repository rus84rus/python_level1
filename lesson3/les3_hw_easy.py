# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

print('\nЗадание - 1.')


def my_func(name, age, city):
    # output = name.title() + ', ', age, 'проживает в городе', city
    output = '{}, {} года(а), проживает в городе {}'.format(name, age, city)
    print(output)
    return output


name = input('Введите свое имя: ')
age = int(input('Введите свой возраст: '))
city = input('Введите свой город: ')

my_func(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

print('\nЗадание - 2.')


def get_max(a, b, c):
    maxnum = a
    if b > a:
        maxnum = b

    if c > maxnum:
        maxnum = c

    print('maxnum =', maxnum)
    return maxnum


get_max(1, 2, 3)
get_max(2, 3, 1)
get_max(3, 2, 1)
get_max(3, 1, 2)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


print('\nЗадание - 3.')

def arg_len(*args):
    biggest = ''
    for i in args:
        if len(i) > len(biggest):
            biggest = i
    print(biggest)
    return biggest

arg_len('абвddddf dsfdfa', 'абвгд', 'ноутбук')