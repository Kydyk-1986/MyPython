#Выведите все элементы, которые меньше 5
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


#for elem in a:
    #if elem < 5:
       # print(elem)

#print(list(filter(lambda elem: elem < 5, a)))


"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(filter(lambda elem: elem in b, a))

print(result)"""

a = 'йцукенгшщзхъфывапролджэячсмитьбю'
y = input('Введите текст:\n')

for i in a:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:

        print('Буква', i, 'использовано', count, 'раза')
