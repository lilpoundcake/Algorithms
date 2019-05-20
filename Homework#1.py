#Задание 6

from math import pow

sum_pow = 0
pow_sum = 0
sum_num = 0

n = int(input("Введите любое натуральное число. "))

for i in range(n, 0, -1):
    sum_pow += pow(i, 2)
    
for i in range(n, 0, -1):
    sum_num += i
    
pow_sum = pow(sum_num, 2)

print('Разность между суммой квадратов от 0 до %i и квадратом суммы от 0 до %i составляет %i.' % (n, n, int(pow_sum - sum_pow)))



#Задание 18
'''Решение универсально как для проблемы 18, так и для проблемы 67'''

pyramid = []

numbers = open('Numbers.txt') 

for lines in numbers:
    pyramid += [lines.strip().split(' ')]

for i in range(len(pyramid)):
    for j in range(i+1):
        pyramid[i][j] = int(pyramid[i][j])

for i in range(len(pyramid)-1, 0, -1):
    for j in range(len(pyramid[i])-1):
        if pyramid[i][j] >= pyramid[i][j+1]:
            pyramid[i-1][j] += pyramid[i][j]
        else:
            pyramid[i-1][j] += pyramid[i][j+1]
print('Максимальная сумма равна', pyramid[0][0], '.')


#Задание 20

from math import factorial

summ_numb = 0
div_ent = 0
div_res = 0

x = int(input('Введите натуральное число. '))
div_ent += factorial(x)

for i in range(len(str(factorial(x)))):
    div_res = div_ent % 10
    div_ent = div_ent // 10
    summ_numb += div_res
    
print('Сумма цифр %i! равна %i.' % (x, summ_numb))
