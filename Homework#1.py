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
max_summ = 0
max_str = 0

numbers = open('Triangle.txt') 

for lines in numbers:
    pyramid += [lines.strip().split(' ')]

for i in range(len(pyramid)):
    max_str = int(pyramid[i][0])
    
    for j in range(len(pyramid[i])):
        if max_str >= int(pyramid[i][j]):
            continue
        else:
            max_str = int(pyramid[i][j])
    
    max_summ += max_str

print('Максимальная сумма в пирамиде сверху вниз составляет %i.' % (max_summ))



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
