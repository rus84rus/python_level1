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
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Денис', 'Сергей', 'Владимир', 'Гвидо']
salaries = ['100500.00', '15000', '999999.99', '654321.321']

person_card = dict(zip(names, salaries))
print('person card =', person_card)

with open('salary.txt', 'w', encoding='utf-8') as file:
    for name, salary in person_card.items():
        file.write('{} - {}\n'.format(name, salary))
print('Конец первой части. Файл записан.')

print('\nВторая часть задачи\n')
with open('salary.txt', 'r', encoding='utf-8') as file:
    line = file.read()
    line = line.strip()
    print(line)
    # print('line strip', line.strip())
print('\nКонец второй части.')

# print('\n Вторая часть задачи решенная циклом\n')
# with open('salary.txt', 'r', encoding='utf-8') as file:
#     dict = {}
    # lines = file.readline()
    # for line in lines:
    #     print(line)
    # for line in file:

        #line = line.split('-')  #line is list
        #print(line[0], line[1])
        # dict[line[0]] = line[1]
        # print(dict)

'''
with open('salary.txt', 'w', encoding='utf-8') as file:
    for name, salary in person_card.items():
        salary = float(salary)              # конвертируем salary из string в float
        salary -= salary*0.13               # вычитаем 13 процентов
        file.write('{} - {}\n'.format(name, salary))
'''