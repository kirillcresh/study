print('''Типы операций поддерживаемых калькуляторов
1.+ сумма
2.- разность
3.* умножение
4./ деление
5.^ воведение числа в степень
6.! факториал числа
7.rand выдает случайное число в диапозоне от 0 до 100
8.acos ищет арккосинус числа
''')
oper = input("Введите операцию ")
if oper == '+':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    print(a + b)
elif oper == '-':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    print(a - b)
elif oper == '*':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    print(a * b)
elif oper == '/':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    print(a / b)
elif oper == '^':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    print(pow(a, b))
elif oper == '!':
    c = int(input("Введите число, для которого нужно найти факториал "))
    import math
    print(math.factorial(c))
elif oper == 'rand':
    import random
    print(random.randint(1, 100))
elif oper == 'acos':
    import math
    x = float(input("Введите число от -1 до 1 ")
    print("ответ в радианах ", math.acos(x)
else:
    print("Ошибка")
input()
