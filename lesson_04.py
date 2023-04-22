## -- FUNCTIONS --
#
# def pattern(length, char2, char1= '*'):
#     return(char1 + char2) * length + char1
# print(pattern(8, '-'))
#
## -- lambda:  functions --
#
# lambda argument: manipulate(argument)
# lambda n: n*n
#
# mult = lambda x, y: x + y
# print(mult(7, 5))

# lst = [20, 'str', 15, 18, 'yes', 'apple', 45]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lst))
# filtered2 = list(filter(lambda x: not isinstance(x, int), lst))
# print(filtered)
# print(filtered2)
#
# map() - modify element of iterable object
# power = list(map(lambda x: x**2 if isinstance(x, int) else x, lst))
# print(power)
#
# reduce() -
# from functools import reduce
# lst = [20, 15, 18, 45]
# res = reduce(lambda x, y: x  * y, lst)
# print(res)
#
## -- DECORATORS --
# function принимает в качестве параметра другую функцию и возвращает функцию
#
# def decorator(function):
#     def wrapper():
#         print('wrapper')
#         print(f'wrapper: {func}')
#         print('run func()')
#         func()
#         print(out of wrapper())
#     return wrapper

# def my_decorator(func):
#     def wrapper(arg):
#         print('Im wrapper')
#         func(arg)
#         print('Wrapper end')
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
# say_hello('John')

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
#
# @sugar
# @milk
# def coffee():
#     print('Coffee')
# coffee()

# import datetime
# bdate = 1980
# current_date = datetime.date.today()
# current_month = current_date.month
# age = current_date.year - bdate
# print(age)
# print(current_month)

# import math as m # alias module

# from module_lesson_4 import hello, summ as s  # * import all modules
# print(hello('Ashley'))
# print(s(10, 55))

## -- NAMESPACES --
# built-in - встроенные объекты
# global - имена на уровне основной программы
# enclosed - имена, определенные внутри внешней функции
# local - переменные, находящиеся внутри функции
#
# print(dir(__builtins__))
#
# var = 'globalvar'
# print(f'globals: {globals()}')
#
# def pattern(length=5, char2='/', char1 = '*'):
#     pattern_1 = (char1 + char2) * length
#     print(f'locals: {locals()}')
# pattern(8, char2='/')
#
# var = 'global'
# def func():
#     var = 'enclosed'
#     def local():
#         var = 'local'
#         print(var)
#     local()
# func()
# print(var)
#
## -- HOMEWORK --
#
# - 4.1
# def square(side):
#     cube = (side * 4, side ** 2, side*(2**0.5))
#     return cube
# print(square(3))
#
# - 4.2
# def person(name, last_name, age, position):
#     print(f'name: {name}\nlast_name: {last_name}\nage: {age}\nposition: {position}')
# person(name='John', last_name = 'Smith', position = 'web-developer', age = '35')
#
# - 4.3
# my_list = [20, -3, 15, 2, -1, -21]
# new = list(filter(lambda x: x > 0, my_list))
# print(new)
#
# - 4.4
#
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# s = reduce(lambda x, y: x * y, my_list)
# print(s)
#
# - 4.5

# def diff(func):
#     import datetime
#     def wrap():
#         start = datetime.datetime.now()
#         func()
#         end = datetime.datetime.now()
#         print(f'Diff: {start} - {end}')
#     return wrap
# @diff
# def valid_parentheses(paren_str):
#     lst = []
#     for i in paren_str:
#         if i == '(':
#             lst.append(i)
#         elif i == ')':
#             try:
#                 lst.pop()
#             except:
#                 return False
#     if len(lst) == 0:
#         return True
#     else:
#         return False
# valid_parentheses('((()()')

# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
# fetch_webpage()


#
# - 4.6
# import sys
# from my_calc import *
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# op = input('Choose operator *, +, -, /: ')
# if op == '+':
#     print(addition(num1, num2))
# elif op == '-':
#     print(subtraction(num1, num2))
# elif op == '*':
#     print(multiplication(num1, num2))
# elif op == '/':
#     if (num2 == 0 and op == '/'):
#         print('На ноль делить нельзя!')
#     else:
#         print(division(num1, num2))


## -- FUNCTION  REVIEW --
#
# def multi(a, b):
#     return (a * b)
# num = multi(5,11) + 10
# num1 = multi(10, 10)
# print(num)
# print(num1)

# def check_even(a):
#     if a % 2 == 0:
#         print('Yes')
#     else:
#         print('No')
# for i in range(15):
#     check_even(i)

# def check_even(a):
#     lst = []
#     for i in range(a):
#         if i % 2 == 0:
#             lst.append('Yes')
#         else:
#             lst.append('No')
#     return lst
# print(check_even(10))

# def fun():
#     s = 'Hi'
#     print(f'Local s: {s}')
# s = 'Bye'
# fun()
# print(f'Global s: {s}')

## -- Recursive --
# def fun(x):
#     if x <= 10:
#         print(x)
#         fun(x+1)
# fun(1)

# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
# print(fact(4))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(3))
#
## -- lambda function --
#
# a = lambda x: x**3
# print(a(3))

# a = [31, 60, 2, 54, 93, 107]
# print(sorted(a, key = lambda x: x % 10)) # по последней цифре
#
# b = ['hello', 'apple', 'xxx', 'bye', 'friday']
# print(sorted(b, key = lambda x: x ))
#
# c = [(1,2), (4,3), (3,1)]
# print(sorted(c, key = lambda x: x[1] ))
#
# d = [(1,'aa'), (3,'bbb'), (3,'bba'), (2,'ss')]
# print(sorted(d, key = lambda x: (x, x[1])))

# e = ['qqq 23', 'qqq 12', 'rrr 8']
# print(sorted(e, key = lambda x: (x.split()[0], int(x.split()[1]))))

## -- MAP() --
#
# a = '1 2 3 4 5 6'
# b = list(map(int,a.split()))
# c = list(map(str,a.split()))
# print(b)
# print(c)

def fun(x):
    return x ** 2

def fun_n(x):
    return x ** 3

# a = [1, 3, 7, 5, -67, -3]

# a1 = list(map(str,a))
# print(a1)
# a2 = list(map(abs,a))
# print(a2)
# a3 = list(map(fun, a))
# print(a3)
# a4 = list(map(fun_n, a))
# print(a4)

# def fun(x):
#     return x > 5
# a = [10, 3, 7, 5, 12, 34]
#
# a1 = list(filter(fun, a))
# a2 = filter(fun, a)
# print(a1)
# print(*a2)

