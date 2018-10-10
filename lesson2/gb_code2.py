# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
# rjust, ljust !!!!

# name = 'Анастасия'
# result = name + '!'
# print(result)
# print(name * 3)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[0:5])
# print(name[2:6])
# print(name[:6])
# print(name[1:])
# print(name[0:-1])
# print(name[::2])
# print(name[::-1])
# print(name[0:6:3])

# name = 'Анастасия'
# index = name.index('ста')
# print(name[index:])
# filename = 'index.html'
# print(filename.split('.'))
# name, extension = filename.split('.')
# print(name, extension)

# name = 'аНаСтАсИя иВаНоВа'
# print(len(name))
# print(name.title())
# print(name.capitalize())
# print(name.startswith('а'))
# print(name.endswith('Ва'))

# name = 'Alex'
# age = 20
# money = 13.43
#
# welcome = 'Привет, тебе лет, у тебя денег'
# print('Привет %s, тебе %i лет, у тебя %f денег' % (name, age, money))
# print('Привет {}, тебе {} лет, у тебя {} денег'.format(name, age, money))
# print(f'Привет {name}, тебе {age} лет, у тебя {money} денег')
# print('Д\'артаньян')
# print("Д'артаньян")

# human = [1, 2, 3, 4, 5, 6, 'qwe', True, 3, 3, 3]
# print(human[0])
# print(human[-1])
# print(human[1:4])
# human[0] = 100
# print(human)

# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html

# human.append('AWDFGH')
# human.insert(0,'AWDFGH')
# print(human.count(3))
# human.remove('qwe')
# deleted = human.pop()
# print(deleted)
# human.pop(1)
# print(human)

# admins = ['Ivan', 'Olga', 'Alex']
#
# if 'Ivan' in admins:
#     print('Иван есть в списке')
#
# if 'Sergey' in admins:
#     print('Сергей есть в списке')
# else:
#     print('Сергея в списке нет!')

# admins = ('Ivan', 'Olga', 'Alex')
#
# i = 0
# while i < len(admins):
#     print(admins[i])
#     i += 1
#
# for name in admins:
#     print(name)
#
# print(name)
#
#
# for number in [1, 2, 3, 4, 5, 6]:
#     print(number ** 2)
#
# for symbol in 'Анастасия':
#     print(symbol)

# admins = ('Ivan', 'Olga', 'Alex')
#
# for index, name in enumerate(admins):
#     print(index, name)
#
# for name in admins:
#     print(admins.index(name), name)

# human = {'name': 'Alex', 'age': 20}
# human2 = {'name': 'Alex', 'age': 20}
# human3 = {'name': 'Alex', 'age': 20}
#
# humans = [human, human2, human3]
# tuple_humans = tuple(humans)
#
# print(tuple_humans)
# print(human['name'])
# print(human['age'])
#
# human['name'] = 'Alice'
# human['money'] = 100.10
# print(human)

# human = {'name': 'Alex', 'age': 20}
# human.pop('name')
# human.popitem()
#
# print(human)

# for key in human.keys():
#     print(key)
#
# for value in human.values():
#     print(value)
#
# for key, value in human.items():
#     print(key, value)

# x = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
# print(x)
#
# y = {'Ivan', 'Alex', 'Ivan'}
# print(y)

# set - множество
# set()
# list()
# tuple()

# a = {1, 2, 3}
# b = {3, 4, 5}
#
# print(a == b)
# print(a <= b)
# print(a >= b)
# print(a | b)
# print(a & b)
# print(a - b)
# print(b - a)
# print(a ^ b)



