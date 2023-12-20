# Необходимо реализовать генератор gen_random(количество, минимум, максимум), 
# который последовательно выдает заданное количество случайных чисел в заданном диапазоне от минимума до максимума, включая границы диапазона

import random

# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел в диапазоне от 1 до 3, например 2, 2, 3, 2, 1

def gen_random(count, minimum, maximum):
    for _ in range(count):
        yield random.randint(minimum, maximum)

for num in gen_random(5, 1, 3):
    print(num)