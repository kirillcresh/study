import math
import random
print('''Типы операций поддерживаемых калькулятором
1.+ сумма
2.- разность
3.* умножение
4./ деление
5.^ воведение числа в степень
6.! факториал числа
7.rand выдает случайное число в диапозоне от 0 до 100
8.acos ищет арккосинус числа
''')
def summ(a,b):
    print(a+b)
def diff(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def power(a,b):
    print(pow(a, b))
def factorial(c):
    pr=1
    for i in range (2,c+1):
        pr=pr*i
    print(pr)
def rand():
    print("Случайное число ", random.randint(1, 100))
def arc(x):
    print("ответ в радианах ", math.acos(x))
oper = input("Введите операцию ")
if oper == '+':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    summ(a,b)
elif oper == '-':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    diff(a,b)
elif oper == '*':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    multiply(a,b)
elif oper == '/':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    div(a,b)
elif oper == '^':
    a = float(input("Введите первое число "))
    b = float(input("Введите второе число "))
    power(a,b)
elif oper == '!':
    c = int(input("Введите число, для которого нужно найти факториал "))
    factorial(c)
elif oper == 'rand':
    rand()
elif oper == 'acos':
    x = float(input("Введите число от -1 до 1 "))
    arc(x)
else:
    print("Ошибка")
input()
