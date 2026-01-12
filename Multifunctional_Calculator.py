import math

import random

def f1(num_1, num_2):
    function_op = int(input("""
Введите операцию:
     1 - Сложение
     2 - Вычитание
     3 - Умножение
     4 - Деление
     5 - Возведение в степень
     6 - Целое деление
     7 - Остаток от деления
     8 - Квадратный корень (только для первого числа) 
     """
     ))
    if function_op == 1:
        print(f"{num_1}+{num_2}={num_1 + num_2}")
    elif function_op == 2:
        print(f"{num_1}-{num_2}={num_1 - num_2}")
    elif function_op == 3:
        print(f"{num_1}*{num_2}={num_1 * num_2}")
    elif function_op == 4:
        print(f"{num_1}/{num_2}={num_1 / num_2}")
    elif function_op == 5:
        print(f"{num_1}^{num_2}={num_1 ** num_2}")
    elif function_op == 6:
        print(f"Ответ равен {num_1 // num_2}")
    elif function_op == 7:
        print(f"Остаток от деления {num_1} и {num_2} {num_1 % num_2}")
    elif function_op == 8:
        print(f"Квадратный корень из {num_1} равен {num_1 ** 0.5}")
    else:
        print(f"Некорректная функция {function_op}")


def f2(num_1, num_2):
    if num_1 > num_2:
        print(f"Число {num_1} больше {num_2}")
    elif num_1 < num_2:
        print(f"Число {num_2} больше {num_1}")
    else:
        print(f"Числа {num_1} и {num_2} равны")


def f3(nums):
    rev = False
    function_sort = int(input("Введите вид сортировки (1 - По возрастанию, 2 - По убыванию) "))
    nums_str = ""
    if function_sort == 2:
        rev = True
    nums.sort(reverse=rev)
    for i in nums:
        nums_str += str(f"{i} ")
    print(nums_str)
    if function_sort not in [1, 2]:
        print(f"Некорректная функция {function_sort}")


def f4(nums):
    print(f"Среднее арифметическое чисел равно {sum(nums) / len(nums)}")


def f5(st_5):
    print(f"Длина строки {st_5} равна {len(st_5)}")


def f6(st_gl_ru):
    gl_ru = "аоуыэяёюеиeuioa"
    st_gl_ru.lower()
    ans_ru = 0
    for i in st_gl_ru:
        if i in gl_ru:
            ans_ru += 1
    if ans_ru > 0:
        print(f"Количество гласных равно {ans_ru}")
    else:
        print("Гласных нет")


def f7(st_sr):
    n_sr = int(input("Введите количество символов, которые нужно оставить "))
    print(st_sr[0:n_sr])


def f8(st_de):
    de = list(map(str, input("Укажите ненужные символы строки через пробел ").split()))
    st_de_new = ""
    for i in st_de:
        if i not in de:
            st_de_new += i
    print(st_de_new)


def f9(st_p):
    n_p = int(input("Введите количество повторений "))
    function_p = int(input("Выберете вид повторения (1 - С пробелами, 2 - Без пробелов) "))
    new_n_p = 0
    if function_p == 2:
        print(st_p * n_p)
    elif function_p == 1:
        st_p_new = ""
        while True:
            if new_n_p < n_p:
                st_p_new += st_p
                st_p_new += " "
                new_n_p += 1
            else:
                print(st_p_new[:len(st_p_new) - 1])
                break
    else:
        print(f"Некорректная функция {function_p}")


def f10(st_iz):
    function_iz = int(
        input("""
Что необходимо сделать:
    1 - Сделать все буквы строчными
    2 - Сделать все буквы заглавными
    3 - Сделать первую букву заглавной
"""))
    if function_iz == 1:
        st_iz_low = st_iz.lower()
        print(st_iz_low)
    elif function_iz == 2:
        st_iz_up = st_iz.upper()
        print(st_iz_up)
    elif function_iz == 3:
        st_iz_up1 = st_iz[0].upper() + st_iz[1:]
        print(st_iz_up1)
    else:
        print(f"Некорректная функция {function_iz}")


def f11(st_de_n):
    st_de_n = list(st_de_n)
    n_de_n = map(int, input("Введите порядковые номера ненужных элементов в одну строку через пробел ").split())
    st_st = ""
    n_de = 1
    g = False
    for i in n_de_n:
        if not i > len(st_de_n):
            g = True
            st_de_n.pop(i - n_de)
            n_de += 1
    for j in st_de_n:
        st_st += j
    if g:
        print(st_st)
    else:
        print("Вы ввели слишком большие порядковые номера")


def f12(s):
    s_s = list(map(str, input("Через пробел введите символы, количество которых нужно посчитать ").split()))
    ans = 0
    for i in s:
        if i in s_s:
            ans += 1
    print(f"Количество символов равно {ans}")


def f13():
    function_dr = int(input("Введите операцию (1 - Сложение, 2 - Вычитание, 3 - Умножение, 4 - Деление) "))
    c_1, ch_1, zn_1 = map(str, input("Введите первую дробь: целая часть (если её нет введите на её место 0) / числитель / знаменатель ").split(" / "))
    c_2, ch_2, zn_2 = map(str, input("Введите вторую дробь: целая часть (если её нет введите на её место 0) / числитель / знаменатель ").split(" / "))
    ch_answ = None
    zn_answ = None
    c_answ = 0
    err = False
    for i in f"{c_1}{ch_1}{zn_1}{c_2}{ch_2}{zn_2}":
        if i not in "0123456789":
            err = True
    if not err:
        c_1, ch_1, zn_1 = int(c_1), int(ch_1), int(zn_1)
        c_2, ch_2, zn_2 = int(c_2), int(ch_2), int(zn_2)
        if function_dr == 1:
            c_answ += c_1
            c_answ += c_2
        elif function_dr == 2:
            c_answ += c_1 - c_2
        elif function_dr in [3, 4]:
            ch_1 += c_1 * zn_1
            ch_2 += c_2 * zn_2
        if function_dr == 1:
            ch_answ = ch_1 + ch_2
            zn_answ = zn_1
        elif function_dr == 2:
            ch_answ = ch_1 - ch_2
            zn_answ = zn_1
        if function_dr == 3:
            ch_answ = ch_1 * ch_2
            zn_answ = zn_1 * zn_2
        elif function_dr == 4:
            ch_answ = ch_1 * zn_2
            zn_answ = zn_1 * ch_2
        de = math.gcd(ch_answ, zn_answ)
        ch_answ //= de
        zn_answ //= de
        while ch_answ >= zn_answ:
            ch_answ -= zn_answ
            c_answ += 1
        print(f"Ответ равен {c_answ} целых, {ch_answ} / {zn_answ}")


def f14():
    function_rand = int(input("Введите вид числа (1 - Целое, 2 - Десятичное) "))
    l_border = str(input("Введите левую границу (ОБЯЗАТЕЛЬНО ЦЕЛОЕ ЧИСЛО) "))
    r_border = str(input("Введите правую границу (ОБЯЗАТЕЛЬНО ЦЕЛОЕ ЧИСЛО) "))
    err = False
    for i in f"{l_border}{r_border}":
        if i not in "0123456789":
            err = True
    if not err:
        l_border = int(l_border)
        r_border = int(r_border)
        if function_rand == 1:
            rand_int = random.randint(l_border, r_border)
            print(rand_int)
        elif function_rand == 2:
            rand_float = random.uniform(l_border, r_border)
            print(str(rand_float).replace(".", ","))
        else:
            print(f"Некорректный вид числа {function_rand}")
    else:
        print("Вы ввели некорректное значение")


def f15():
    function_pass = int(input(
        "Введите вид пароля (1 - Со словом, 2 - Только цифры (Не рекомендуется использовать как реальный пароль)) "))
    if function_pass == 1:
        name = "_"
        name += input("Введите ваше имя (можно псевдоним, сокращённое имя, просто слово и т.д.) ")
    elif function_pass == 2:
        name = ""
    while True:
        pass_rand = random.randint(100000, 99999999)
        if len(set(str(pass_rand))) >= 6:
            print(f"{pass_rand}{name} - Ваш надёжный пароль")
            break


def f16(num):
    function_per = int(input("Введите вид перевода (1 - Из любой в десятичную, 2 - Из десятичной в любую) "))
    ans = None
    if function_per == 1:
        num = str(num)
        s_sch_iz = int(input("Введите систему счисления, из которой хотите перевести "))
        ans = int(num, base=s_sch_iz)
        print(f"Число {num} в системе счисления {s_sch_iz}, это {ans} в десятичной")
    elif function_per == 2:
        s_sch_v = int(input(
            "Введите систему счисления, в которую хотите перевести (2 - Двоичная, 8 - Восьмиричная, 16 - Шестнадцатиричная) "))
        if s_sch_v == 2:
            ans = str(bin(num))[2:]
        elif s_sch_v == 8:
            ans = str(oct(num))[2:]
        elif s_sch_v == 16:
            ans = str(hex(num))[2:].upper()
        print(f"Число {num} в системе счисления {s_sch_v}, это {ans}")
    else:
        print(f"Некорректный вид перевода {function_per}")


def f17(num):
    print(f"Число {num} в научной записи, это {num:E}")


def f18(num):
    print(f"Факториал числа {num} равен {math.factorial(num)}")


def f19():
    function_fib = str(input("""Выберите действие: 
    1 - Вывести ряд чисел Фибоначчи с заданным количеством чисел.
    """))
    err = False
    for i in function_fib:
        if i not in "0123456789":
            err = True
    if not err:
        function_fib = int(function_fib)
        if function_fib == 1:
            ans = ""
            num_fib = int(input("Введите длину ряда чисел Фибоначчи "))
            start_fib = [0, 1]
            if num_fib <= 2:
                for j in start_fib:
                    j = str(j)
            elif num_fib > 2:
                for i in range(2, num_fib):
                    ch_fib = start_fib[i - 2] + start_fib[i - 1]
                    start_fib.append(ch_fib)
                for j in start_fib:
                    j = str(j)
            for h in start_fib:
                ans += str(h)
                ans += " "
            print(ans)
    else:
        print("Вы ввели некорректное значение")


def f20(num_1, num_2):
    print(f"НОД {num_1} и {num_2} равен {math.gcd(num_1, num_2)}")


version = "4.0"
print(f"Добро пожаловать в Многофункциональный калькулятор (да и не только), версия {version}")
super_function = int(input(
    """Выберите функцию:
    0 - Информация о проекте
    1 - Операции с числами,
    2 - Сравнение чисел,
    3 - Сортировка чисел,
    4 - Вычисление среднего арифметического,
    5 - Вычисление длины строки,
    6 - Нахождение количества гласных букв,
    7 - Срез строки,
    8 - Убрать ненужный символ(-ы) в строке,
    9 - Повторение строки,
    10 - Изменение строки по высоте букв,
    11 - Удалить символ(-ы) по его порядковому номеру
    12 - Нахождение числа нужного(-ых) символа(-ов),
    13 - Операции с дробями,
    14 - Генератор рандомных чисел,
    15 - Генератор надёжного пароля,
    16 - Перевод числа в разные системы счисления,
    17 - Переписать число в научную запись,
    18 - Вычисление факториала заданного числа,
    19 - Действия с числами Фибоначчи,
    20 - Вычисление НОД двух чисел.
    """))

if super_function in [1, 2, 20]:
    num_1 = str(input("Введите первое число "))
    num_2 = str(input("Введите второе число "))
    err = False
    for i in num_1:
       if i not in "0123456789.":
           err = True
    for i in num_2:
        if i not in "0123456789.":
            err = True
    if not err:
        num_1 = float(num_1)
        num_2 = float(num_2)
        if num_1 % 1 == 0:
            num_1 = int(num_1)
        if num_2 % 1 == 0:
            num_2 = int(num_2)
        if super_function == 1:
            f1(num_1, num_2)
        elif super_function == 2:
            f2(num_1, num_2)
        elif super_function == 20:
            f20(num_1, num_2)
    else:
        print("Вы ввели некорректное значение")
elif super_function in [3, 4]:
    nums = list(map(str, input("Введите числа в одну строку через пробел ").split()))
    err = False
    for num in nums:
        for j in num:
            if j not in "0123456789.":
                err = True
    if not err:
        for num in nums:
            num = float(num)
        if super_function == 3:
            f3(nums)
        elif super_function == 4:
            f4(nums)
    else:
        print("Вы ввели некорректное значение")
elif super_function in [5, 6, 7, 8, 9, 10, 11, 12]:
    st = input("Введите строку ")
    if super_function == 5:
        f5(st)
    elif super_function == 6:
        f6(st)
    elif super_function == 7:
        f7(st)
    elif super_function == 8:
        f8(st)
    elif super_function == 9:
        f9(st)
    elif super_function == 10:
        f10(st)
    elif super_function == 11:
        f11(st)
    elif super_function == 12:
        f12(st)
elif super_function in [13, 14, 15, 19]:
    if super_function == 13:
        f13()
    elif super_function == 14:
        f14()
    elif super_function == 15:
        f15()
    elif super_function == 19:
        f19()
elif super_function == 0:
    print("""
Название проекта - Многофункциональный калькулятор
Версия - 4.0(release)
Начало разработки проекта - 2 ноября 2025 года
Последняя версия выпущена - 8 января 2026 года
Многофункциональный калькулятор не хранит данные о пользователях, мы заботимся о вашей конфиденциальности, все данные после нового запуска программы стираются
Что нового в последних версиях:
    1. Добавлена функция 18.
    2. Добавлена функция 19.
    3. Изменён вывод результата в функции 1.
    4. Добавлена функция 20.
    5. Завершение разработки первой фазы проекта, добавление проверок.
    """)

elif super_function in [16, 17, 18, 19]:
    num = int(input("Введите число "))
    if super_function == 16:
        f16(num)
    elif super_function == 17:
        f17(num)
    elif super_function == 18:
        f18(num)
else:
    print(f"Некорректная функция {super_function}")