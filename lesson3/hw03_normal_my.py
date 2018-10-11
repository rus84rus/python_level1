# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко,
# используя возможности языка Python.
import os

humans = ['Алиса', 'Иван', 'Роман']
salaries = [33000, 80000, 70000]
nalog = 13


# открывает указанный файл и записывает в него словарь любой длины в два столбца: ключ - значение

def write_dict_to_file(file, **kwargs):
    with open(file, 'w', encoding='utf-8') as file:
        for key, value in kwargs.items():
            file.write('{} - {}\n'.format(key, value))


# читает файл с данными (имя - зарплата), создает словарь: имя: зарплата ( за минусом 13%)

def read_file_output(file, nalog):
    with open(file, 'r', encoding='utf-8') as file:
        dict_read = {}
        for line in file.readlines():
            keys, value = line.strip().split(' - ')
            dict_read[keys] = (float(value) - (float(value)) * nalog / 100)
            # dict_read = dict.fromkeys([keys], value)
            # print(type(line))
            # print(line)
            # dict_read = {keys: value keys, value = (line.strip().split(' - '))}

        # print(dict_read)
    return dict_read


# фильтрует данные из словаря по заданной зарплате

def dict_filtred(set_filtred=50, **kwargs):
    dict_filtr = {}
    for key, value in kwargs.items():
        if float(value) < set_filtred:
            dict_filtr[key] = value
    # print(dict_filtr)
    return dict_filtr


# выводит данные из словаря в верхнем регистре

def up_reg(**kwargs):
    temp_dict = {}
    for key, value in kwargs.items():
        key = key.upper()
        temp_dict[key] = value
    print(temp_dict)
    return temp_dict


# создадим словарь: имя - зарплата
salary_dict = dict(zip(humans, salaries))

# запишем словарь в файл salary.txt
write_dict_to_file(('files/salary.txt'), **salary_dict)

# прочитаем файл и вычтем налог
dict_salary_nalog = read_file_output('files/salary.txt', nalog)

# отфильтруем словарь по зарплатам
dict_filtr = dict_filtred(40000, **dict_salary_nalog)

# выведем данные словаря со значениями в верхнем реигистре

dict_up = up_reg(**dict_filtr)
