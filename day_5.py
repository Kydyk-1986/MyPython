# Списки (List)
#a = [13, 1432, 'gsdfg', 'wgwerg', ['wregw', 35245234, ['wergre']], 13, 123, 'wger',]
#s = [1231, 344564, 345]
# s.append(12)
# s.extend(a)
# s.insert(2, 543)
# s.remove(34)
# s.pop(2)
# print(a.index(element, start, stop))
# print(a.count(13))
# s.sort()
# d = s.copy() # [*s]
# print(d)
# a[4] = 'asdf'
# print(a)

"""1. Вам дан кортеж. Вывести его в обратном порядке.
('n', 'o', 'h', 't', 'y', 'p', ' ', ',', 'u', 'o', 'y', ' ', 'e', 'v', 'o', 'l', ' ', 'i')"""

"""a = ('n', 'o', 'h', 't', 'y', 'p', ' ', ',', 'u', 'o', 'y', ' ', 'e', 'v', 'o', 'l', ' ', 'i')
d = a(str)
print(type(a))"""



"""2. Вам дан список. Поменяйте местами второй и последний элементы, а затем удалите последний элемент.
['Am', 'I', 'a', 'good', 'programmer', '?']"""

""""a = ['Am', 'I', 'a', 'good', 'programmer', '?']
a[1], a[5] = a[5], a[1]
print(type(a))
a.pop(5)
print(a)"""



"""3. У вас есть желание найти бесполезное число. Возьмите произвольный список из чисел. Найдите самое большое значение из них и поделите его на длину списка.
"""

"""a = [12, 34, 423, 4324]
print(max(a)/len(a))"""

"""4. Напишите скрипт, который запрашивает у пользователя число. Ваша задача создать кортеж из любых уникальных значений, длина которого будет равна запрашиваемому числу.
"""

"""import random

a = int(input("Введите число до 6: "))
b =  ["dfdfdffd", "dfdfdfd", "gdfgdg", "dfdfdf", 1324, 'bgbd']
random.shuffle(b)
c = []
for element in range(a): # range(3) --> (0, 1, 2)
    c.append(b[element])
print(tuple(c))"""

"""5. У вас есть список из строк. Ваша задача найти самую длинную, затем привести каждую остальную строку к такой же длине заполняя их символом "_".
['Something', 'in', 'the', 'way', 'mmmmmmm', 'btw', 'python', 'is', 'better', 'than', 'js']"""

s = ['Something', 'in', 'the', 'way',
     'mmmmmmm', 'btw', 'python', 'is',
     'better', 'than', 'js']
smax = max(s, key=len)
print(smax)
"""for i in range(len(s)):
    while len(s[i]) < len(smax):
        s[i] += '_'"""
#print(s)