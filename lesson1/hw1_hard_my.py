# -*- coding: utf-8 -*-
# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
# Пример: Владимир Медведев, 22 лет, вес 33 - Вы слишком мало весите, обратитесь к врачу

print ("Медицинская анкета")
name = input("Введите ваше имя:")
sername = input("Введите вашу фамилию:")
age = int(input("Введите ваш возраст:"))
weith = int(input("Введите ваш вес:"))

if age < 30 and (weith > 50 and weith < 120):
        print(name, sername, ",", age, "год", ",", "вес", weith, "- хорошее состояние")
elif (age >= 30 and age <= 40) and (weith < 50 or weith > 120):
        print(name, sername, ",", age, "год", ",", "вес", weith, "- следует заняться собой")
elif age > 40 and (weith < 50 or weith > 120):
        print(name, sername, ",", age, "год", ",", "вес", weith, "- следует обратиться к врачу")
elif age > 30 and (weith > 50 and weith < 120):
        print(name, sername, ",", age, "год", ",", "вес", weith, "- Рустам это ты?")
elif age < 30 and weith < 50:
        print(name, sername, ",", age, "год", ",", "вес", weith, "- Не льсти себе, Рустамджан?")
else:
    print("Ввел что то не то")
