## -- OBJECT ORIENTED PROGRAMMING --
# __init_() method constructor of class
# self.color - dynamic
# def.color - static
# class Dog:
#     # static attribute
#     biology_class = 'Animal'
#
#     # dynamic attribute
#     def __init__(self, name, weight, color):
#         self.name = name
#         self.weight = weight
#         self.color = color
#
#     def run(self):
#         return 'I can run'
#
#     def get_name(self):
#         return f'Hello! My name is {self.name}'
#
# dog1 = Dog('Bob', 3, 'brown') #объект класса Dog
#
# print(dog1.name)
# print(dog1.color)
# print(dog1.run())
# print(dog1.get_name())
# print(dog1.biology_class)
#
# dog2 = Dog('Rex', 7, 'black')
# print(dog2.name)
# print(dog2.get_name())
# print(dog2.biology_class)
#
# ## -- OOP Concepts - INHERITANCE --
#
# class Pitbull(Dog):
#     def __init__(self, name, weight, color, passport):
#         super().__init__(name, weight, color)
#         self.passport = passport
#
#     def give_a_paw(self):
#         return 'I can give a paw'
#
#     def run(self):
#         return 'I can run fast'
#
# dog3 = Pitbull('Jake', 8, 'grey', 'type1')
# print(dog3.passport)
# print(dog3.biology_class)
# print(dog3.give_a_paw())
# print(dog3.get_name())
# print(dog3.run())

## -- OOP Concepts - POLYMORPHISM--
# class Dog:
#     def __init__(self, name, weight, color):
#         self.name = name
#         self.weight = weight
#         self.color = color
#
#     def run(self):
#         return 'I can run'
#
# class Pitbull(Dog):
#     def __init__(self, name, weight, color, passport):
#         super().__init__(name, weight, color)
#         self.passport = passport
#
#     def run(self):
#         return 'I can run fast'
#
# dog2 = Dog('Rex', 7, 'black')
# dog3 = Pitbull('Jake', 8, 'grey', 'type1')
#
# print(dog2.name)
# print(dog2.run())
# print(dog3.name)
# print(dog3.run())

## -- OOP Concepts - ENCAPSULATION --
# Data = variables
# Code = methods
# Class = variables + methods

# class Dog:
#     def __init__(self, name, weight, color):
#         self._name = name
#         self.weight = weight
#         self.color = color
#     def get_name(self):
#         return f'Hello! My name is {self._name}'
#     def set_name(self, new_name):
#         self._name = new_name
#
# dog2 = Dog('Rex', 7, 'black')
# print(dog2.get_name())
# print(dog2.__dict__)
#
# print(dog2.set_name('Snoopy'))
# print(dog2.get_name())
# print(dog2._name)

## GIT - Version Control Service --
