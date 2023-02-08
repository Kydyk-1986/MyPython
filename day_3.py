# name = "15151345145"
# name2 = name.title()
# name2 = name.upper()
# name2 = name.replace('1', 'One')
# v = (name + name2) * 10
# print(name2)

# [index] Индекс
# [start:stop:step] Срез
# len() Длина строки


str1 = input()
str2 = input()
print(f"{str1} amazing {str2}") # Новый способ форматирования
print("{} amazing {}".format(str1, str2)) # Использовался до Python 3.7
print("%s amazing %s" % (str1, str2)) # Самый старый способ форматирования (до Python 2.7)