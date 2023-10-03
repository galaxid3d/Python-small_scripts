# 18.04.2015 by galaxid3d
# Переводит арабское число в греческое

"""
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
"""

def dec_to_greek(dec_number, greek_number):  # dec_number - десятичное число, greek_number - греческая ТСДЕ (тысяча, сотня, десяток, еденица)
    greek_chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    t = greek_chars.index(greek_number)
    if dec_number in range(1, 4):
        print(dec_number * greek_chars[t], end="")
    elif dec_number == 4:
        print(greek_chars[t], end="")
        print(greek_chars[t + 1], end="")
    elif dec_number in range(5, 9):
        print(greek_chars[t + 1], end="")
        print(greek_chars[t] * (dec_number - 5), end="")
    elif dec_number == 9:
        print(greek_chars[t], end="")
        print(greek_chars[t + 2], end="")

greek_chars = ['I', 'X', 'C', 'M']  # список из греческих - тысячи, сотни, десятки, единицы
number = int(input('Введи число: '))
if number > 0 and number < 4000:
    if number < 10: n = 1
    elif number < 100: n = 2
    elif number < 1000: n = 3
    else: n = 4
    a = []
    number = str(number)
    for x in range(n):  # делает список из цифр числа
        a.append(int(number[x:x+1]))
    for i in range(n):
        dec_to_greek(a[i], greek_chars[n - i - 1])  # Посылает в функцию количество Т/С/Д/Е и определение какого разряда идёт (Т/С/Д/Е)
else:
    print('Такого греческого числа нет', end="")
