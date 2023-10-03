# 08.03.2015 by galaxid3d
# Рисует на экране числа и буквы как в Матрице

import random
import time

# это генератор второго столбика: 8 случайных символов (числа от 1 до 9 или заглавные английские буквы)
def print_8_numbers_or_chars():
    for _ in range(8):
        number = random.randrange(0, 10)
        char = random.randrange(65, 91)
        probability = random.randrange(1, 4)
        if probability % 3 == 0:
            print(chr(char), end="")
        else:
            print(number, end="")

# это генератор со второго по четвёртый столбик (т.к второй, третий, четвёртый и пятый столбики состоят из 8 символов)
def print_4_cols():
    for _ in range(4):
        print_8_numbers_or_chars()
        print("  ", end="")

# это генератор шестого столбика: 18 случайных символов (числа, точка, пробел, английские буквы)
def print_18_random_chars():
    char_space = " "
    char_dot = "."
    print("[", end="")
    for _ in range(16):
        number = random.randrange(10)
        char_small = random.randrange(97, 123)
        char_big = random.randrange(65, 91)
        probability = random.randrange(1, 6)
        if probability == 1: print(char_space, end="")
        elif probability == 2: print(char_dot, end="")
        elif probability == 3: print(chr(char_small), end="")
        elif probability == 4: print(chr(char_big), end="")
        elif probability == 5: print(number, end="")
    print("]", end="")

rows_count = int(input("Пиши сколько строк будет: "))
row = 0
str_zero = '0000'
str_zero_count = len(str_zero)
for i in range(rows_count):
    if row < 100:
        print(str_zero[:1] + str_zero if row < 10 else str_zero, end="")
    elif row < 1000:
        print(str_zero[:str_zero_count - 1], end="")
    elif row < 10000:
        print(str_zero[:str_zero_count - 2], end="")
    elif row < 100000:
        print(str_zero[:str_zero_count - 3], end="")
    elif row < 1000000:
        print(str_zero[:str_zero_count - 4], end="")

    print(row, end="")
    print(':', end="  ")
    print_4_cols()
    print_18_random_chars()
    print()
    row = row + 10
    time.sleep(0.01)
