## LISTS - списки
# набор или последовательность элементов. Изменяемая структура данных.
# # Create a list:  option 1 - []
# my_list = [1, 'hello', 2.2, True, None]
# print(my_list)
# # Create a list:  option 2
# sentence = 'Python is awesome'
# print(sentence.split(' '))

# # list index
# print(my_list[0])
# print(my_list[-1])

# # change 0-index
# print('Before',my_list)
# print(id(my_list))
# my_list[0] = 25
# print('After',my_list)
# print(id(my_list))

# # lists method
# .append() - add element to end of the list
# .insert() - add element to certain place of the list
# .index() - to get element index
# .clear() - to clear list
# .remove() - to remove element from plistlib
# .reverse() - to reverse the order of the list
# .count() - to return the number of elements with the specified value
# .sort() - to sort list
# .min() -

# my_list.append(sentence)
# print(my_list)
# print(len(my_list))

# my_list.insert(-1, sentence)
# print(my_list)

# print(my_list.index(None))
# print(my_list.count(1))

# my_list1 = [1,2,3,4,5]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))
#
# my_list2 = [1,2,3,4,5, [1,2,3,4, [1,2]]]
# print(my_list2[-1])
# print(my_list2[-1][-1][1])

# my_list2.reverse()
# print(my_list2)

## For loop with list
# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num*2)
# # List comprehension
# numbers = [1,2,3,4,5]
# new_l = []
# for x in numbers:
#     if x%2:
#         new_l.append(x*x)
# print(new_l)
#
# new_l2 = [x*x for x in numbers if x%2]
# print(new_l2)
#
## TUPLES - кортежи
# элементы разделяются запятыми, строки в кавычках, числа без кавычек
# неизменяемая структура
# tuple = (1,2,3)
# Create tuples:
# brackets (); tuple();
#
# # Create tuple:
# my_tuple = 1, 2, 3
# print(my_tuple)
#
# my_tuple2 = (1, True, 'name', 4, None, 'family')
# print(my_tuple2)
#
# name = 'Mark',
# print(name)
# print(type(name))

# fruits = ('apple', 'banana', 'cat')
# a, b, c = fruits
# print(a)
# print(b)
# print(c)
#
# fruits = ('apple', 'banana', 'cat')
# fruits_list = list(fruits)
# fruits_list[0] = 'ananas'
# print(fruits)
# print(fruits_list)
#
# # Getting index of items
# my_tuple = (1, True, 'name', None, 'family', 'name', 25)
# print(my_tuple[2])
# print(my_tuple.count('name'))
# print(my_tuple.index('name'))
#
# Filtering in Tuple
# my_tuple = (1, True, 'name', None, 'family', 'name', 25)
# result  = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)
#
# # Tuple Methods
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tuple is: {len(my_tuple)}')
# print(f'Length of result is: {len(result)}')
#
# Iterate tuple with for loop
# for(index, item) in enumerate(my_tuple):
#     print(index,item)
#
# Iterate tuple with while loop
# i = 0
# while i < len(my_tuple):
#     print(i,my_tuple[i])
#     i += 1
# # Nested list in tuple - можно менять элемент вложенного листа
# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)
#
# # Swap variables
# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')
#
# # Passing tuple as an argument in function
# def sum_it(*args):
#     total =0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     print(len(args))
#     for i in args:
#         l.append(i*i)
#     return l
# print(func(2, 5, 6, 8, 10))
#
# DICTIONARY - словари
#  набор элементов, где каждый элемент имеет пару ключ - значение
# dictionary = {key1: item1, key2: item2}
# Create dictionary:
# my_dict = {}; my_dict = dict()
# ключи - строки, числа
# значение - любой тип
# изменяемая структура
#
# my_dict = {'name': 'Anna', 'last_name': 'Pavlova', 'age': '30', 'department': 'IT'}
# print(my_dict)
# print(id(my_dict))
# print(my_dict['name'])
# my_dict['last_name'] = 'Smirnova'
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))
# my_dict['salary'] = 5000  # add new item
# print(my_dict)
#
# # Methods
# .keys() - output only keys
# .items() - create tuple with keys and values
# .get() - get value by key
# .clear() - to clear dictionary
# .copy() - to copy dictionary
# .pop() - to output item and remove from dictionary
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict.get('salary', 'Not found'))
#
# Create dict with zip - function
# keys = ['name', 'salary', 'department']
# values = ['Alex', 4000, 'HR']
# employee = dict(zip(keys, values))
# print(employee)
#
# employee1 = dict(name='John', position='developer', salary = 6000, department='IT')
# print(employee1)
# SETS - множества
# как словарь без значений. Ключи уникальны.
# my_set = {'A', "B", 'C'}
# Create set:
# my_set{A', "B", 'C'}; my_set = set{}
# удобно удалять дубли из списка
#
# my_list = [10, 8, 20, 1, 5, 5, 10, 3, 8, 9]
# print(set(my_list))
#
# set1 = {1,2,3, 'one', 'ten'}
# set2 = {1,2,3, 'one', 'ten', 100, 525}
# set3 = {1,2,3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set3))
# print(set1.symmetric_difference(set2))
#
# print(set1)
# print(id(set1))
# set1.remove(1)
# print(set1)
# set1.add(8)
# print(id(set1))
# print(set1)
#
# fs = frozenset({1, 2, 3})
# print(fs)
#
# ========
# HOMEWORK
# - 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])
# print((my_list[2][0]),(my_list[2][1]), (my_list[2][2]))
# print(my_list[2])
#
# - 3.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# s = []
# for x in list_1:
#     if type(x) == int:
#         s.append(x)
#
# print(sum(s))
# for w in list_1:
#     if type(w) == str and 'a' in w:
#         print(w)

#
# - 3.3
# list = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list))
#
# - 3.4
# fam1 = str(input('Write fam1: '))
# fam1_list = fam1.split(',')
# fam2 = str(input('Write fam2: '))
# fam2_list = fam2.split(',')
# if len(fam1_list) > len(fam2_list):
#     print(fam1_list)
# elif len(fam1_list) < len(fam2_list):
#     print(fam2_list)
# else:
#     print('Equal')
#
# - 3.5
# film = dict(title='Titanic', director='James Cameron', actor='Leonardo di Caprio', actress='Kate Winslet', year = '1997')
# print(film)
# print(film.keys())
# print(film.values())
# print(film.items())
#
# - 3.6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# - 3.7
# list = [1, 2, 3, 4, 5, 3, 2, 1]
# list = set(list)
# print(list)
#
# - 3.8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
#
# ======
#
# - LIST REVIEW -- brackets
# lst = [1, 2, 'as', False,[1, 2, 5]]
# lst1 = []
# lst2 = list(range (4))
# print(lst2 + lst)
# print(2 in lst)
# if 5 in lst:
#     print('yes')
# else:
#     print('no')
# print(lst[4][1])
# lst = [1, 4, 3, 5, 19, 10]
# print(sum(lst))
# print(min(lst))
# print(max(lst))
# print(sorted(lst))
# print(lst.sort())
# lst1 = ['Anna', 'Dima']
# lst.extend(lst1)
# print(lst)
# del lst[0]
# print(lst)
# lst.remove(3)
# print(lst)
# lst.pop()
# print(lst)
# lst.reverse()
# print(lst)
# lst1 = lst.copy()
# lst2 = lst
# lst[0] = 6
# print(lst)
# print(lst1)
# print(lst2)
#
# TUPLES REVIEW -- parenthesis
#
# tuple = (1, 2, 3, 4)
# tuple1 = sorted(tuple)
# print(tuple)
# print(tuple1)
#
# SET REVIEW -- braces
# set = {1, 1, 3, 5, 5, 7, 9}
# # print(set)
# # print(len(set))
# # print(max(set))
# # print(sum(set))
# set.add(22)
# print(set)
# lst = ['hello', 55, False]
# set.update(lst)
# print(set)
# set может update вложенный tuple, но не вложенный list
# set = {3, 5, 7, 9}
# set1 = {44, 5, 6, 9}
# a = set.union(set1)
# b = set.intersection(set1)
# c = set.difference(set1)
# d = set.symmetric_difference(set1)
# print(f'union {a}')
# print(f'intersection {b}')
# print(f'difference {c}')
# print(f'sym-difference {d}')

# num = {int(i) for i in input()}
# print(num)
# number = int(input())
# num1 = {i for i in range(number)}
# print(num1)

# DICTIONARY REVIEW -- braces
#
# dct = {'Russia': '+7', 'USA': '+1', 'Turkey': '+90'}
# print(dct)
# dct2 = dict(Russia = +7, USA = +1, Turkey = +90)
# print(dct2)
# if 'USA' in dct2:
#     print('yes')
# else:
#     print('no')
# dct = {'name': 'Anna', 'age': '19'}
# dct1 = {'country': 'Russia', 'city': 'Tula'}
# dct2 = dct|dct1
# print(*dct2, sep='\n')

# for key, value in dct2.items():
#     print(key, value)



















