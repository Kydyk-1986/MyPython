"""PROBLEM 8:

Найдите, какой процент этого столетия мы прожили:

формула расчета процентов

(a/b)*100

где a-прожитые года

b-сколько нужно(тк. это столетие,

b-100)"""

years_old = int(input('Введите число '))
year_3 = int(input('Введите второе число '))

stoletiya = (years_old / year_3) * 100
result_3 = ' % проижили'
result_4 = 'Ответ: '

print(result_4 + str(stoletiya) + result_3)