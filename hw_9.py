"""PROBLEM 9:

Создать 2 переменные.

В первой год вашего рождения, Во второй

2022 год

посчитайте сколько лет вам должно быть через 2 года/и сколько лет вам было два года назад"""

a = int(input('Введите год вашего рождения '))
b = int(input('Введите нынешний год '))

year = 'сейчас Вам '
year_1 = ' лет, '
after = 'а через 2 года Вам будет '
age = b - a

print(year + str(age) + year_1 + after + str(age + 2))