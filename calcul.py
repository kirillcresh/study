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
    x = float(input("Введите число в радианах "))
    print(math.acos(x))
else:
    print("Ошибка")
input()
