import math
import random
def summ(a,b):
    print(a+b)
def diff(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def pow(a,b):
    print(pow(a, b))
def factorial(c):
    pr=1
    for i in range (2,c+1):
        pr=pr*i
    print(pr)
def rand():
    print(random.randint(1, 100))
def arc(x):
    print(math.acos(x))
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
    pow(a,b)
elif oper == '!':
    c = int(input("Введите число, для которого нужно найти факториал "))
    factorial(c)
elif oper == 'rand':
    rand()
elif oper == 'acos':
    x = float(input("Введите число в радианах "))
    arc(x)
else:
    print("Ошибка")
input()
