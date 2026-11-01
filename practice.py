# name = 'Faraz Kazi'
# age = 28
# salary = 250000.4505
# u
# # print(f"(Employe is {name} and salary :₹{salary: .2f}")
# userAge =  input ('Enter you age')
# convertAge = int(userAge) + 5
#
# if convertAge == 18:
#   print ('You are an adult')
# elif convertAge <= 10:
#     print ('You are child')
#
# elif convertAge >= 50:
#     print("your are old now")
#
# else:
#     print ('You are ready to die')
from typing import cast
from unittest import result


# for i in range(6):
#     print(i)
#
# for i in range(2, 15, 2):
#     print(i)

# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1

# emplyess =  ['faraz','Danish', 'Amsh']
# emplyess.append('Faiz')
# emplyess.remove('Danish')
# emplyess[2] = 'Faaz'
# print (len(emplyess))
# print(emplyess)
#
# number = [5,1,3,1,1]
#
# for x_count in number:
#     print(x_count * '*')
# number = [2, 4, 6]
# # number.append(1)
# #
# # for n in number:
# #   print(n)

# number = [2, 4, 6, 60, 12, 45, 56]
# print(number[-5:-1])
# # print(number[0:2])
# ---tupel
# numbers = (10, 12, 13 , 14 )
# print(numbers[0])

# Converting tupel to list

# numbers = (10, 20, 30)
#
# my_list = list(numbers)
# my_list.append(40)
#
# numbers = tuple(my_list)
#
# print(numbers)
# tuple unpacking
# student = ("Ali", 25, "Engineer")
#
# name, age, profession = student
#
# print(name)
# print(age)
# print(profession)
#
# person = ("Ravi", 30, "Engineer")
# name, age = person
# print(name)
# print(age)

# ---SET---
# numbers = {10, 20, 10, 30, 20}
# print(numbers)
# numbers = {10, 20}
# numbers.update([30, 40, 50])
# print(numbers)
# numbers = {10, 20, 30}
# numbers.discard(50)  # No error, even though 50 is missing
# numbers.remove(20)
#
# print(numbers)
# fruits = {"apple", "banana", "mango"}
#
# for fruit in fruits:
#     print(fruit)

# student = set()
# print(type(student))

# counting = {10, 20, 30}
#
# counting.add(10)
#
# counting.update({40, 50})
#
# print(counting)

# cities = {"Osmanabad", "Pune", "Mumbai"}
# for city in cities:
#      print(city)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print(A | B)
# print(A.union(B))
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print(A & B)
# print(A.intersection(B))

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print(A - B)
# print(B - A)
#
# ---- Dictionary---

# studenst = {
#     'name': 'Faraz Kazi',
#     'age': 21,
#     'city': "osmanabad"
# }
# studenst['course'] = 'Python'
# print(studenst)
# print(studenst["name"])
# print(studenst["age"])
#
# student = {
#     "name": "Farhan",
#     "age": 22,
#     "city": "Osmanabad"
# }
#
# removed_age = student.pop("age")
#
# print(removed_age)
# print(student)
#
# for key, value in student.items():
#     print(key, ":", value)
#
# data = {"a": 10, "b": 20}
# print(list(data.keys()))
#
# student = {
#     "name": "Ali",
#     "age": 20
# }
#
# student.update({
#     "age": 22,
#     "city": "Osmanabad"
# })
#
# print(student)

# students = {
#     "student1": {
#         "name": "Ali",
#         "age": 20
#     },
#     "student2": {
#         "name": "Sara",
#         "age": 22
#     }
# }
#
# (students['student2']['name']) = "Faraz"
# print(students['student2']['name'])

# name = "Faraz Kazi Alemm"
#
# print(name[0:4])
# print(name[:])
# print(name[:8])
# print(name[::4])
# print(name[::-1])

# ---FUNCTION---
#
# def greeting():
#     print("hello world")
#
# greeting()
#
# def calculate_total():
#     price1 = 100
#     price2 = 200
#     print(price1 + price2)
#
# calculate_total()

# def greeting(name, age):
#     print(f"Hello, {name}, you are {age} years old")
#
# greeting('Faraz', 27)
# greeting('Danish', 35)

# def add(a,b):
#     print(a+b)
#
# result = add(12, 15)
#
# print(result)

# def sum(a, b):
#     return a * b
#
# add(15, 5)
#  ---- defulat value---
# def greet(name, message="Hello"):
#     print(message, name)
#
# greet("Ali")
#
# def calculate_price(price, tax=0.05):
#     return price + (price * tax)
#
# print(calculate_price(100))
# print(calculate_price(100, 0.10))


# def details (name, age, city):
#     print(name, age, city)
#
# details(name='Faraz kazi', age = 27, city= 'Pune')
# details('Faraz Kazi', age = 28, city= "osmanabad")
#
# def calculate_salary(name, salary, bounus = 2000):
#     total_salary = salary + bounus
#     return total_salary
#
# result = calculate_salary('Faraz Kazi', salary=40000, bounus= 4000)
#
# print(result)

# def add(*args):
#     total = 0
#
#     for number in args:
#         total = total + number
#
#     return total
#
# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(10, 20, 30, 40, 50))

# def add(*args):
#     return sum(args)
#
# print(add(2, 3, 5))

# def greet():
#     message = "Hello"
#     print(message)
#
# greet()
# name = "Ali"
#
# def greet():
#     print(name)
#
# greet()
# print(name)

# count = 10
#
# def update():
#     count = 20
#     print(count)

# update()
# print(count)
#
# count = 10
#
# def update():
#     global count
#     count = 20
#
# update()
# print(count)

# Returning Multiple Values----

# def calculate_number(a,b):
#     sum  = a + b
#     sub = a - b
#
#     return sum, sub
# result = calculate_number(10,2)
# sum_result, difference_result = calculate(10, 3)
#
# print(sum_result)
# print(difference_result)
#
# print(result)
#
# def employee_payment(salary, bonus):
#     total = salary + bonus
#     return salary, total
#
# basic_salary, total_payment = employee_payment(30000, 5000)
#
# print("Basic salary:", basic_salary)
# print("Total payment:", total_payment)

# Lambda functioin ----

# add_ten = lambda x: x + 10
# print(add_ten(5))

# import math
#
# print (math.sqrt(64))
#
# from math import sqrt
#
# print(sqrt(125))

# import datetime
#
# today = datetime.datetime.today()
# today = datetime.datetime.now()
# print(today)
# Data Engineering connection: Later, you can use os to locate data files and organize file-processing tasks.
#
# import os
#
# print(os.getcwd())

# Import a module with an alias ----

# import datetime as dt
#
# today = dt.date.today()
# # print(today)
#
# def add(a, b):
#     return a + b

# def calculation_number (a,b):
#     return a + b
# # result   = calculation_number(1,2)
# #
# # print(result)
#
# import math
#
# print(dir(math))

# import json
#
# person = {
#     "name" : "Faraz Kazi",
#     "age" : 25,
#     "city" : "osmanabd"
# }
#
# result = json.dumps(person)
#
# print(type(person))
# print(type(result))

#
# import json
#
# data = '{"name": "Ali", "age": 25}'
#
# person = json.loads(data)
#
# print(person)
# print(person["name"])
#
# # exception handling ----
# name = int(input("enter number"))
# print(name)
#
# try :
#     number = int(input("ENter number"))
#     print(number)
#
# except ValueError:
#     print("Enter a valid number.")

# try:
#     number = int(input("Enter a number: "))
#     print(100 / number)

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(result)
#
# except ValueError:
#     print("Please enter a valid number.")
#
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
#
# try:
#     salary = float(input("Enter your salary: "))
#     print(salary)
# except ValueError:
#     print("Please enter a number")
# else:
#     bonus = salary * 0.10
#     print(f" you bonus is {bonus}")

# class----
#
# class Cars:
#     def __init__(self, brand, clour):
#         self.brand = brand
#         self.clour = clour
#
#
# car1 = Cars("TATA", 'black')
# car2 = Cars("Maruti", "White")
#
# print(car1.brand, car1.clour,  car2.brand, car2.clour)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calculte_bouns(self):
#         bouns = self.salary * 0.10
#         print("Employee:", self.name,"\n""Slalary:", self.salary)
#         print ("Bouns: ", bouns)
#
# emp_1 = Employee("Faraz Kazi", 10000)
# emp_2 = Employee("Danish kazi", 20000)
#
# emp_1.calculte_bouns()
# emp_2.calculte_bouns()

# class Faraz:
#     faraz_adress = "xyz"
#     def __init__(self, name, wight, heghit, age):
#         self.name = name
#         self.wight = wight
#         self.heghit = heghit
#         self.age = age
#
#     def allinformation(self):
#         return self.name, self.wight, self.heghit, self.age
# faraz1 = Faraz("Faraz",60, 173, 28)
#
# print(faraz1.allinformation())

# class Acoount:
#     def __init__(self, bal, acc):
#         self.baalance = bal
#         self.acc = acc
#
#     def Crediet(self, amount):
#         self.baalance += amount
#         print("rs", amount, "credit")
#         print("current balance is", self.get_balance())
#
#     def debaite(self,amount):
#         self.baalance -= amount
#         print("rs", amount, "debate")
#         print("current balance is", self.get_balance())
#     def get_balance(self):
#         return self.baalance
#
#
#
# acc1 = Acoount(10000, 7869)
# acc1.Crediet(100)
# acc1.debaite(200)
# acc1.get_balance()

# class Car:
#     def __init__(self, type):
#         self.type = type
#
#     @staticmethod
#     def start():
#         print("car start")
#
#     @staticmethod
#     def stop():
#         print("car stop")
#
# class Toyotacar(Car):
#      def __int__(self,type):
#          super().__init__(type)
#          super().start()
#
#
# car1 = Toyotacar("Electiical")
# print(car1.type)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property

    def parcentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stud1 = Student(89, 90, 95)
stud1.chem = 95
stud1.math = 50
print(stud1.parcentage)

print(stud1.parcentage)