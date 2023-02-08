"""a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

if a > b:
    print('Переменнея ', a, ' больше')

elif a < b:
    print('Переменнея ', b, ' больше')"""

# Вторая задача

"""a_1 = int(input('Введите любое число '))

if a_1 % 2 == 0:
    print('Вы ввели четное число ', a_1)
else:
    print('Вы ввели нечетное число, поэтому возведем в квадрат', a_1**2)"""


#Третья задача

"""km = int(input('Расстояние до бабушки '))

if km < 2:
    print('Пойдешь пешком')
elif km < 12:
    print('Поедешь на велосипеде')
else:
    print('На машине')"""

#Четвертая задача


"""Heals = int(input('Введите число здоровье '))
Uron = int(input('Введите число урона '))

if Heals > Uron:
    print('Человек жив')
elif Heals < Uron:
    print('Челове умер')"""

#Пятая задача

win = [12, 1, 2]
spr = [3, 4, 5]
summ = [6, 7, 8]
out = [9, 10, 11]

monthe = int(input('Вводим месяч '))

if monthe in win:
    print('Белый снег ')
elif monthe in spr:
    print('Чумачедчая весна ')
elif monthe in summ:
    print('На Иссык-Куль ')
elif monthe in out:
    print('Пусть бегут ')
else:
    print('Такого месяца не существует ')