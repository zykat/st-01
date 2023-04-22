# === Lesson 2 ===
#
# Comparison operators
# x = 5
# print(x > 3 and x < 8) #true
# print(x > 3 or x < 8) #true
# print(not x > 5) #true
# print(not x == 5) #false
# print(x > 3 and x > 8) #false
# print(x > 3 or x > 8) #true
# print(x < 3 and not x < 8) #false

# == Conditional and logical statements

# == IF - ELSE cycle ===

# num = int(input("enter digit: "))
# if num == 5:
#     print("Yeah, it's five!")
# else:
#     print('not equal to 5')

# num = int(input("enter digit: "))
# if num == 5:
#     print("Yeah, it's five!")
# elif num > 5:
#     print('It is more than 5')
# else:
#     print('Less than 5')

# currentYear = 2023
# birthYear = int(input("Enter your birth year: "))
# age = currentYear - birthYear
# if age > 18:
#     print(f'You are {age} years old, so welcome! Have a pleasure!')
# else:
#     print(f'You are too young to be here. Come later, in {18 - age} years')


# import sys
# try:
#     num1 = int(input('Enter number1: '))
#     num2 = int(input('Enter number2: '))
# except ValueError:
#     print('Вы ввели не число!')
#     sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/'):
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# elif(operator == '/'):
#     result = num1 / num2
#     print(f'Result = {result}')
# elif(operator == '*'):
#     result = num1 * num2
#     print(f'Result = {result}')
# elif(operator == '+'):
#     result = num1 + num2
#     print(f'Result = {result}')
# elif (operator == '-'):
#     result = num1 - num2
#     print(f'Result = {result}')
# else:
#     print('Не верный оператор!')

# == WHILE - cycle ===

# num = 1
# while num < 5:
#     print(num)
#     num += 1 # num = num + 1

# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print(i, message, message)
#         continue
#     print(i, message)
#
# x = 0
# i = 0
# while i < 4:
#     x += i # 0 1 3 6
#     i += 1 # 1 2 3
#     print(f'x = {x}, i = {i}')

# === FOR cycle ===
# for i in range(1, 6, 1):  # range(start,stop,step)
#     print(i)

# for i in 'Hello':
#     print(i)
#
# message = 'Hello'
# print(message[0: 5: 2])

# num = 9
# if num%2 != 0:
#     print('Нечетное')
# else:
#     print('Четное')

# === Functions ===
#
# x = int(input('enter number1: '))
# y = int(input('enter number2: '))

# def sum(x,y):
#     return x + y
# print(sum(x,y))
# start = sum(x,y)
# for i in range(start, 20, 2):  # range(start,stop,step)
#     print(i)
#
# =======
#
## HOMEWORK ##
# - 2.1
# import sys
# try:
#     health = int(input('Enter health procent: '))
# except ValueError:
#     print('Вы ввели не число!')
#     sys.exit()
# if health > 71 and health <= 100:
#     print('You are STRONG!')
# elif health >= 30 and health <= 70:
#     print('You are OK')
# elif health <= 29 and health >= 5:
#     print('You are weak')
# elif health == 0 or health < 0:
#     print('You are DEAD, sorry')
# else:
#     print('Are you still breathing?')



# - 2.2
# num = int(input('Enter your digit: '))
# if num%2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# - 2.3 -
# year = int(input('Enter your year:'))
# if year % 4 == 0 or year == 500 or year == 600:
#     print('Високосный')
# elif year % 400 == 0:
#     print('Високосный')
# else:
#     print('Невисокосный')
#

# - 2.4 -
# t = (input('Enter your text:'))
# re = int(input('Enter number of repeat:'))
# i = 1
# while i <= re:
#     print(t)
#     i += 1

# - 2.5 -
# import sys
# try:
#     num1 = int(input('Enter number1: '))
#     num2 = int(input('Enter number2: '))
# except ValueError:
#     print('Вы ввели не число!')
#     sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/'):
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# elif(operator == '/'):
#     result = num1 / num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif(operator == '*'):
#     result = num1 * num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif(operator == '+'):
#     result = num1 + num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif (operator == '-'):
#     result = num1 - num2
#     print(f'{num1} {operator} {num2} = {result}')
# else:
#     print('Не верный оператор!')
#
# =========
#
## REVIEW
#
# s = 'hello world'
# print(s.replace('o', 'u'))
# print(s.replace('l', '&', 2)) # 2 appearance
# print(s.count('o'))

# s = 'Johnson John Johnovich'
# print(s.split())
# print(s.split('o')) # split by symbol

# s = '1, 2, 3, 4, 5'
# #print(s.split(',', maxsplit= 3))
# print(s.split(','))
#
# s1 = s.split(',')
# print(''.join(s1))

# w = '      hello      '
# print(w)
# print(w.strip())
#
# w1 = '      123hello123      '
# print(w1)
# print(w1.strip())
# print(w1.strip().strip('123'))
#
# w2 = 'hello world'
# print(w2.find('e')) ## symbol-index
# print(w2.find('o', 2, 5)) ##if no symbol - output: -1
#
# print(w2.index('e')) #if no symbol - output: Substring not found
#
# s4 = 'name'
# s5 = 'FaMilY'
# s6 = 'gloBal woRld championat'
# print(s4.upper())
# print(s5.lower())
# print(s6.title())
# print(s6.capitalize())
# print(s6.swapcase())

# s7 = 'qwerty'
# s8 = 'QWERTY'
# r7 = '1234'
# r8 = '1234asdfg'
# d7 = '01234'
# d8 = '0,9'
# d9 = '1234R'
# print(s7.islower()) #true
# print(s8.islower()) #false
# print(r7.islower()) #false
# print(r8.islower()) #true
# print(s7.isupper()) #false
# print(s8.isupper()) #true
# print(d7.isdigit()) #true
# print(d8.isdigit()) #false
# print(d9.isdigit()) #false
#
# =========
#
# == CYCLES ===
# a = int(input('Enter digit: '))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f'{a} делится на 2 и на 10')
#     else:
#         print(f'{a} делится на 2, но не делится на 10')
# else:
#     print(f'{a} не делится на 2')

# x, y = 55, 57
# s = x if x > y else y
# print(s)
#
# if x > y:
#     print(x)
# else:
#     print(y)


# value = 4
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print("Wrong value")

# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Chet')
#     else:
#         print('Nechet')
#     c += 1

# text = int(input('Enter num: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('To continue enter num, to stop - enter stop: ')
# print(f'Sum of nums is {count}')

# num = 10
# for i in range(1, num+1, 2):
#     print(i)

# str_1 = 'hello'
# for s in range(len(str_1)):
#     print(s)

# str_1 = 'hello'
# for s in range(len(str_1)):
#     print(str_1[s])
# same
# str_1 = 'hello'
# for s in str_1:
#     print(s)

# str_1 = 'HeLlo'
# for i in range(len(str_1)):
#     if str_1[i].islower():
#         print(i, str_1[i])
#
# ======
#
# == CODEWARS ==
#

