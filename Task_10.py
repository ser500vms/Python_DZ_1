# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 - > 1 0 1 1 0
# 2

import random

n = int(input('Введите количество монет: '))
coins = []
i = 0
eagle = 1
count_eagle = 0
count_tails = 0

for _ in range(n):
    coins.insert(i, random.randint(0, 1))
print(f'{n} -> {coins}')

for _ in range(n):
    if coins[i] == eagle:
        count_eagle += 1
        i += 1
    else:
        count_tails += 1
        i += 1
if count_eagle < count_tails:
    print(f'Нужно перевернуть {count_eagle} монет с орлом')
else:
    print(f'Нужно перевернуть {count_tails} монет с решкой')