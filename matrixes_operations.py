# 27.10.2015 by galaxid3d
# Модуль для вычисления различных операций над матрицами

"""
Структура программы:
    - Вводим операцию
    - Запускается функция ввода матрицы.
        По завершению:
        - Запускается функция выполнения операций над матрицами.
            По завершению:
            - Запускается функция вывода матрицы
"""

# ~объявление функций идёт в обратном порядке (не в порядке выполнения), т.к. ф-ия сначала должна быть объявлена, а затем использована

#   Функция вывода матрицы   #
def matrix_output(M, show=False):
    if type(M) == list:
        minors = True  # переменная, которая хранит: выводить сейчас миноры или нет
        try:
            M[0][0][0][0]  # если в списке(матрице) ещё 3 списка, то это минорная матрица
        except:
            minors = False  # если не получилось зайти в 4 список, то это простая матрица (2 списка)
        if not minors:  # если выводим не минорную матрицу (т.к. для неё свой (особый) способ вывода)
            if type(M[0][0]) == float:  # если элементы массива списка - это числа (т.к. при несуществующей обратной матрице возвращается пустая (из символов ""))
                if not show:
                    print('Получившаяся матрица:')
                else:
                    print('Вы ввели матрицу:')
                for j in range(len(M)):  # количество строк
                    for i in range(len(M[0])):  # количество столбцов (оно одинаково у всех строк, поэтому не важно M[0] выберем или другой индекс)
                        t = M[j][i]
                        if int(t) == t:
                            print(int(t), end=" ")  # если число целое, то выводим без запятой
                        else:
                            print(t, end=" ")
                    print()
        elif type(M[0][0][0][0]) == float:  # если минорная матрица
            print('Получившаяся матрица:')
            for j in range(len(M)):
                # Важно! мы должны сначала в одну строку вывести только первую строку минорной матрицы,
                # а у нас все строки хранятся в одном списке, поэтому поменял очерёдность циклов
                # (сначала 'for k', а потом 'for i', хотя печать результата прежняя: M[j][i][k][l])
                for k in range(len(M[0][0])):
                    for i in range(len(M[0])):
                        for l in range(len(M[0][0][0])):
                            t = M[j][i][k][l]
                            if int(t) == t:
                                print(int(t), end=" ")
                            else:
                                print(t, end=" ")
                        print("", end=" ")  # ставим пробелы между столбцами минорной матрицы
                    print()  # переводим курсор на новую строку
                print()  # ставим пустую строку между строками минорной матрицы
    else:
        print('Определитель матрицы:', M)

#   Функция операций над матрицами   #  
def matrix_calc(op_name, M1, M2, a, sign, power):
    # Сложение/Вычитание
    def matrix_calc_summa(M1, M2, sign):
        # тут и далее не обязательно заполнять нулями, т.к. мы всё равно каждый эл-т будем заменять,
        # главное, чтобы хоть чем-то заполняли при генерации списка
        result = [[0 for i in range(len(M1[0]))] for j in range(len(M1))]
        for j in range(len(M1)):  # количество строк (оно одинаково у обеих матриц, т.к. делали list_slice())
            for i in range(len(M1[j])):  # количество столбцов (тоже одинаково)
                result[j][i] = M1[j][i] + sign * M2[j][i]
        return result

    # Умножение
    def matrix_calc_multi(M1, M2):
        result = [[0 for i in range(len(M2[0]))] for j in range(len(M1))]  # новая матрица будет из (n_1*m_2)-элементов
        for j in range(len(M1)):
            for i in range(len(M2[0])):
                tmp = 0
                for k in range(len(M1[0])):
                    # т.к. любой элемент получившейся матрицы вычисляется
                    # (M1*M2)[j][i]=M1[j][1]*M2[1][j]+M1[j][2]*M2[2][j]+...+M1[j][количество столбоц первой/либо строк второй]*M2[n_1/m_2][j]
                    tmp = tmp + M1[j][k] * M2[k][i]
                result[j][i] = tmp
        return result

    # Умножение на число
    def matrix_calc_multi_a(M, a):
        result = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for j in range(len(result)):
            for i in range(len(M[0])):
                result[j][i] = M[j][i] * a
        return result

    # Возведение в натуральную степень
    def matrix_calc_power(M, N):
        result = M
        for n in range(N - 1):  # "-1",т.к. у нас сразу идёт перемножение (т.е. возведение в квадрат)
            result = matrix_calc_multi(result, M)
        return result

    # Транспонирование
    def matrix_calc_transpose(M):
        result = [[0 for i in range(len(M))] for j in range(len(M[0]))]
        for j in range(len(M[0])):  # т.к. в транспонированной кол-во строк = кол-ву столбцов исходной
            for i in range(len(M)):
                result[j][i] = M[i][j]
        return result

    # Нахождение обратной матрицы
    def matrix_calc_inverse(M):
        # создаём все эл-ты - "", а не нули,
        # т.к. у нас будет вывод этой матрицы на экран в любом случае, поэтому пустая матрица правильнее нулевой
        result = [['' for i in range(len(M[0]))] for j in range(len(M))]
        det = matrix_calc_determinant(M)
        if det == 0:
            print('Обратной матрицы не существует')
        else:
            M_join = matrix_calc_transpose(matrix_calc_alg_apps(M))  # создаём присоединённую матрицу
            result = matrix_calc_multi_a(M_join, (1 / det))
        return result

    # Нахождение миноров
    def matrix_calc_minors(M):
        # создаём матрицу размера-n, каждый элемент которой является матрицей размера-(n-1)
        result = [[[[0 for l in range(len(M[0]) - 1)] # "-1", т.к. размер новой матрицы будет меньше на 1, т.к. мы вычёркмваем 1 строку и 1 столбец
                    for k in range(len(M) - 1)]
                   for i in range(len(M[0]))] for j in range(len(M))]
        # циклы перебора всех элементов результирующей матрицы
        for j in range(len(M)):
            for i in range(len(M[0])):
                aa = bb = -1  # при переходе к новому эл-ту минорной матрицы, "обнуляем" счётчики номера эл-та, который мы записали в result (т.е. на котором остановились)
                for k in range(len(M) - 1):
                    for l in range(len(M[0]) - 1):
                        next = False  # переменная, от которой зависит: переходить нам к следующему элементу минорной матрицы или нет
                        # циклы перебора исходной матрицы
                        for a in range(len(M)):
                            if a < aa: continue  # если мы не дошли до строки, на которой остановились, то берём следующую строку. "<" - значит, что мы можем продолжать с той строки, на которой остановились
                            for b in range(len(M[0])):
                                if b <= bb: continue  # если не дошли до столбца (эл-та), на котором остановились,то берём следующий. "<=" - значит, что мы НЕ можем продолжать с того столбца (эл-та), на котором остановились
                                if a != j and b != i:  # если сейчас "невычеркнутая" строка и "невычеркнутый" столбец, т.е. нельзя брать те же индексы, что у текущего минора и у эл-та исходной матрицы,который мы сейчас проверяем
                                    result[j][i][k][l] = M[a][b]
                                    next = True  # если записали в result эл-т исходной матрицы, то берём следующий эл-т минорной матрицы
                                    aa = a  # запоминаем на какой строке остановились
                                    bb = b  # запоминаем на каком столбце остановились
                                if next == True: break  # если записали что-то в result, то дальше столбцы (эл-ты) исходной м-цы для этого минорного эл-та не проверяем и переходим к след.эл-ту минорной м-цы
                            if next == True: break  # если записали что-то в result, то дальше строки для этого минорного эл-та не проверяем
                            bb = -1  # при переходе на новую строку, "обнуляем" номер столбца(эл-та) исходной м-цы на котором мы остановились
        return result

    # Нахождение алгебраических дополнений
    def matrix_calc_alg_apps(M):
        result = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for j in range(len(M)):
            for i in range(len(M[0])):
                result[j][i] = ((-1) ** (j + i + 2)) * matrix_calc_determinant(matrix_calc_minors(M)[j][i])
        return result

    # Нахождение определителя
    def matrix_calc_determinant(M):
        if len(M) == 1 and len(M[0]) == 1: return M[0][0]  # если матрица из одного элемента, то определитель равен самому эл-ту
        # ф-ция будет работать и без этой строчки, но с ней считает в (1.25-2) раза быстрее. В 2 раза - для малньких ф-ций (2x2),а в 1.25 раза-для больших (6x6)
        if len(M) == 2 and len(M[0]) == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
        result = stroka = 0
        zeromax = M[0].count(0)
        for j in range(1, len(M)):  # определяем в какой строке больше нулей, чтобы быстрее считать (особенно для больших матриц с большими коэффициентами)
            if M[j].count(0) > zeromax:
                zeromax = M[j].count(0)
                stroka = j
        for i in range(len(M[0])):
            result = result + M[stroka][i] * ((-1) ** (stroka + i + 2)) * matrix_calc_determinant((matrix_calc_minors(M)[stroka][i]))
        return result

    if op_name == "summa": return matrix_calc_summa(M1, M2, sign)
    if op_name == "multi": return matrix_calc_multi(M1, M2)
    if op_name == "multi_a": return matrix_calc_multi_a(M1, a)
    if op_name == "power": return matrix_calc_power(M1, power)
    if op_name == "transpose": return matrix_calc_transpose(M1)
    if op_name == "inverse": return matrix_calc_inverse(M1)
    if op_name == "minors": return matrix_calc_minors(M1)
    if op_name == "alg_apps": return matrix_calc_alg_apps(M1)
    if op_name == "determinant": return matrix_calc_determinant(M1)

#   Функция ввода матриц   #
def matrix_input(op):
    # обрезает количество элементов массива до k, если их ввели больше k,добавляя нейтральный элемент n для операции,и просит ввести недостающие эл-ты,если для этой операции нейтрального эл-та нет
    def list_slice(a, k, n, second_input=False):  # заранее присвоение переменной значения значит, что мы можем вызывать ф-цию и без неё, т.е. с 2 параметрами, а если введём третий, то он заменит присвоенное значение
        length_a = len(a)
        if length_a > k:
            aa = []
            for i in range(k): aa.append(a[i])
        else:
            aa = a
            if not second_input:
                for i in range(k - length_a):  # если нехватка элементов, то добавляем нейтральный (n)
                    aa.append(n)
            else:
                while len(a) != k:
                    print('Вы ввели не все элементы этой строки. Введите недостающие:')
                    for i in range(length_a, k):
                        aa.append(float(input('Введите недостающий элемент:')))
        return aa

    def matrix_input_summa(sign):
        m = int(input('Введите количество строк матриц: '))
        n = int(input('Введите количество столбцов матриц: '))
        print('Введите элементы первой матрицы через пробел:')
        M1 = [list_slice(list(map(float, input().split())), n, 0) for j in range(m)]  # Вводим строку (числа через пробел) столько раз, сколько m
        print('Введите элементы второй матрицы через пробел')
        M2 = [list_slice(list(map(float, input().split())), n, 0) for j in range(m)]
        matrix_output(M1, True)
        matrix_output(M2, True)
        return matrix_calc("summa", M1, M2, 0, sign, 0)

    def matrix_input_multi():
        m_1 = int(input('Введите количество строк первой матрицы: '))
        n_1 = int(input('Введите количество столбцов первой матрицы: '))
        m_2 = int(input('Введите количество строк второй матрицы: '))
        n_2 = int(input('Введите количество столбцов второй матрицы: '))
        while n_1 != m_2:
            print('Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы')
            n_1 = int(input('Введите количество столбцов первой матрицы: '))
            m_2 = int(input('Введите количество строк второй матрицы: '))
        print('Введите элементы первой матрицы через пробел:')
        M1 = [list_slice(list(map(float, input().split())), n_1, 1) for j in range(m_1)]
        print('Введите элементы второй матрицы через пробел')
        M2 = [list_slice(list(map(float, input().split())), n_2, 1) for j in range(m_2)]
        matrix_output(M1, True)
        matrix_output(M2, True)
        return matrix_calc("multi", M1, M2, 0, 0, 0)

    def matrix_input_multi_a():
        m = int(input('Введите количество строк матрицы: '))
        n = int(input('Введите количество столбцов матрицы: '))
        print('Введите элементы матрицы через пробел')
        M = [list_slice(list(map(float, input().split())), n, 1) for j in range(m)]
        a = float(input('Введите число: '))
        matrix_output(M, True)
        return matrix_calc("multi_a", M, 0, a, 0, 0)

    def matrix_input_power():
        n = int(input('Введите размерность матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, 1) for j in range(n)]
        N = int(input('Введите степень: '))
        matrix_output(M, True)
        return matrix_calc("power", M, 0, 0, 0, N)

    def matrix_input_transpose():
        m = int(input('Введите количество строк матрицы: '))
        n = int(input('Введите количество столбцов матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, '', True) for j in
             range(m)]  # т.к. для транспонирования нет нейтрального элемента,то просим ввести заново
        matrix_output(M, True)
        return matrix_calc("transpose", M, 0, 0, 0, 0)

    def matrix_input_inverse():
        n = int(input('Введите размерность матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, '', True) for j in range(n)]
        matrix_output(M, True)
        return matrix_calc("inverse", M, 0, 0, 0, 0)

    def matrix_input_minors():
        m = int(input('Введите количество строк матрицы: '))
        n = int(input('Введите количество столбцов матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, '', True) for j in range(m)]
        matrix_output(M, True)
        return matrix_calc("minors", M, 0, 0, 0, 0)

    def matrix_input_alg_apps():
        m = int(input('Введите количество строк матрицы: '))
        n = int(input('Введите количество столбцов матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, '', True) for j in range(m)]
        matrix_output(M, True)
        return matrix_calc("alg_apps", M, 0, 0, 0, 0)

    def matrix_input_determinant():
        n = int(input('Введите размерность матрицы: '))
        print('Введите элементы матрицы через пробел:')
        M = [list_slice(list(map(float, input().split())), n, '', True) for j in range(n)]
        matrix_output(M, True)
        return matrix_calc("determinant", M, 0, 0, 0, 0)

    if ("+" in op): return matrix_input_summa(1)
    if ("-" in op) and ("-1" not in op): return matrix_input_summa(-1)  # смотря какой знак, то на этот множитель (1/-1) умножаем второе слагаемое у матриц
    if ("*" in op) and (("**" not in op) and ("*a" not in op)): return matrix_input_multi()
    if ("*a" in op): return matrix_input_multi_a()
    if ("**" in op): return matrix_input_power()
    if ("T" in op): return matrix_input_transpose()
    if ("-1" in op): return matrix_input_inverse()
    if ("M" in op): return matrix_input_minors()
    if ("A" in op): return matrix_input_alg_apps()
    if ("det" in op):
        return matrix_input_determinant()
    else:
        print('Такой операции нет')
        return [['']]

print('Возможные операции:')
print("  ", "+   (сложение матриц)")
print("  ", "-   (вычитание матриц)")
print("  ", "*   (умножение матриц)")
print("  ", "*a  (умножение матриц на число)")
print("  ", "**  (возведение матрицы в натуральную степень)")
print("  ", "T   (транспонирование матрицы)")
print("  ", "-1  (нахождение обратной матрицы)")
print("  ", "M   (нахождение всех миноров матрицы)")
print("  ", "A   (нахождение всех алгебраических дополнений матрицы)")
print("  ", "det (нахождение определителя матрицы)")
op = str(input('Введите операцию: '))
matrix_output(matrix_input(op))