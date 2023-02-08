# password = input("Придумайте пароль: ")
# password2 = input("Повторите пароль: ")

# if len(password) >= 8 and len(password) <= 16:

#     if password == password2:
#         print('Успех!')
#     else:
#         print("Пароли не совпадают")

# elif len(password) < 8:
#     print("Слишком короткий пароль")

# else:
#     print("Длина пароля не должна превышать 16 символов!")

"""a = 'hELlo woRLd'

a = a[0:5].title() + ' ' + a[6:].upper()

print(a)"""

""".3 Вам даны две строки. Нужно найти есть ли одна строка в другой строке вне
зависимости от регистра. Если есть вывести "Есть", иначе "Нет"."""

"""a = input('Пишите строку первую ')
b = input('Пишите строку вторую ')
a = a.lower()
b = b.lower()

if a in b:
    print('Есть')
else:
    print('Нет')"""

"""glas = 'уеаоиэ'
sl = input('Любое слово пиши ')

if sl[-2] in glas:
    print(sl[-2] * 16)"""

#5. Вам дана строка в camelCase - "pythonIsTheBestLanguage". Вывести ее в snake_case.

camelCase = "pythonIsTheBestLanguage"
snake_case = camelCase.replace('pythonIsTheBestLanguage', 'python_Is_The_Best_Language')
print(snake_case)








