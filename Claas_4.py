#1. Дан диапазон чисел от 1 до 1000. Вывести все четные числа которые делятся на 7 без остатка.

"""for i in range(1, 1000):
    if i % 2 == 0: #or and i % 7 == 0
        if i % 7 == 0:
             print(i)"""

#2. Дана строка 'abcdefghijklmnopqrstuvwxyz'. Вывести порядковый номер, главную и
#заглавную букву алфавита.

"""a_1 = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(a_1)):
    print('Индекс', i, 'и соостветстующий символ',  a_1[i])"""


"""team1 = []
team2 = []
epople = ['epople'] * 15
for i in range(1, len(epople)):
    if i % 2 == 0:
        team1.append(epople[i])
    else:
        team2.append(epople[i])
print(team1)
print(team2)"""


"""3. У вашего игрового персонажа есть шкала энергии, которая равна 1000 единиц. И у вас есть
определенные активности, которые забирают у вас энергию. 1 - спорт (100 единиц), 2 -
домашняя активность (60 единиц), 3 - уроки (180 единиц), 4 - слушать нытье(200 единиц).
Так же есть активности, которые дают вам энергию: 1 - прослушивание музыки (60 единиц),
2 - прием пищи (150 единиц), 3 - сон (500 единиц).

Задача: пользователь должен сам выбирать активности до тех пор, пока не закончится
энергия. Вывести на сколько в общем было потрачено энергии и сколько восполнено."""




"""health = 1000
dream = 500
lessons = 580

while health > 0:
    action = input('Выберите действие: ')
    if action == dream:
        health -= lessons
        print(f'Heelth: {health}' )
else:
    print(f'Fatality: {health}') !!!"""


health = 1000
dream = 500
lessons = 580

while health > 0:
    print("Доступные действия: dream(+500), lessons(-180)")
    action = input("Выберите действие: ")
    if action == 'lessons':
        health -= lessons
        print(f"Health: {health}")
    else:
        print("Введите корректные данные!")
else:
    print(f'Fatality! Health: {health}')