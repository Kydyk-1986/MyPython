"""PROBLEM 2:

Создайте 4 условия:

1.Число А больше В но меньше С.

2. Результат деления по модулю числа 7 на 3 умножить на 4.8

3.Создать два разных выражения которые равны друг другу.

4. Создать 2 выражения которые  НЕ равны друг другу."""


a = int(input('Введите переменную (a) '))
b = int(input('Введите переменную (b) '))
c = int(input('Введите переменную (c) '))

if a < b:
    a > c
    a = c
    a = b
    c = b
    print('Заданные значении не соответствуют a > b и a < c')
elif a == b == c:
    print('Заданные значении не соответствуют так как a == b == c')
else:
    print('Введенные значении ', a > b, a < c, ' соответствуют требованию a > b < c')


po_module = 7 % 3 * 4.8

print('Результат по модулю ', po_module)

a_1 = int(input('Введите первое число '))
a_2 = int(input('Введите второе число '))
b_1 = int(input('Введите первое число '))
b_2 = int(input('Введите второе число '))
result = a_1 + a_2
result_1 = b_1 + b_2

if result > result_1:
    print('Выражении не равны друг к другу так как a_1 + a_2 > b_1 + b_2')
elif result < result_1:
    print('Выражении не равны друг к другу так как a_1 + a_2 < b_1 + b_2')
else:
    print('Выражении равны друг к другу a_1 + a_2 == b_1 + b_2')


a_3 = 4 + 7
a_4 = 4 + 8

print('Выражении не равны друг к другу ', a_3, '<', a_4)



