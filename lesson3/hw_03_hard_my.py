# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# player_stats = {'name': 'person1', 'health': '120', 'damage': '10'}
# enemy_stats = {'name': 'person2', 'health': '100', 'damage': '30'}
# players = {'player': player_stats, 'enemy': enemy_stats}
#
# print(players)
#
#
# def attack(person_1, person_2):
#     damage = int(players.get(person_1)['damage'])
#     health = int(players.get(person_2)['health']) - damage
#     print(damage, health)
#     players[person_2]['health'] = str(health)
#
#
# attack('player', 'enemy')
#
# print(players)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
## после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

# player_1=input('Введите имя игрока 1:')
# player_2=input('Введите имя игрока 2:')
player_stats = {'name': 'person1', 'health': '140', 'damage': '10', 'armor': '1.2'}
enemy_stats = {'name': 'person2', 'health': '100', 'damage': '30', 'armor': '2.9'}
players = {'player': player_stats, 'enemy': enemy_stats}

# сохраним игроков в файлы (имя_игрока.тхт)

name_file_1 = ('files/players/' + players.get('player')['name'] + '.txt')
name_file_2 = ('files/players/' + players.get('enemy')['name'] + '.txt')
with open(name_file_1, 'w', encoding='utf-8') as file:
    for key, values in players['player'].items():
        file.write('{} - {}\n'.format(key, values))
with open(name_file_2, 'w', encoding='utf-8') as file:
    for key, values in players['enemy'].items():
        file.write('{} - {}\n'.format(key, values))

    # print(players)


# функция считывает файлы игроков и заносит данные игроков в словари

def read_file_create_dict(file_1, file_2):
    dict_tmp_1 = {}
    dict_tmp_2 = {}
    with open(file_1, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            key, val = line.strip().split('-')
            dict_tmp_1[key] = val
    with open(file_2, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            key, val = line.strip().split('-')
            dict_tmp_2[key] = val
    return (dict_tmp_1, dict_tmp_2)


# функция вычисляет урон который может нанести атакующий исходя из брони атакуемого и возвращает модифицированный урон

def damage_attack(person_1, person_2):
    damage = float(person_1.get['damage']) / float(person_2.get['armor'])
    # print(damage)
    return damage


# функция вычитает урон атакующего из здоровья атакуемого
def attack(person_1, person_2):
    damage = damage_attack(person_1, person_2)
    health = float(person_2.get['health']) - damage
    # print(damage, health)
    person_2['health'] = str(health)


# создадим словари с данными игроков

player, enemy = read_file_create_dict(name_file_1, name_file_2)
print(player, enemy)

# запустим игровой процесс

while True:
    attack(player, enemy)
    if float(enemy['health']) <= 0:
        print('Победил игрок: ' + player_1, 'Оставшееся здоровье: ' + player['health'])
        break
    attack(enemy, player)
    if float(player['health']) <= 0:
        print('Победил игрок: ' + player_2, 'Оставшееся здоровье: ' + player['health'])
        break

print(players)
