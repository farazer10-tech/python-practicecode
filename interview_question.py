# Q1)--
# x = 5
# print(type(x))

# Q2)--- Access element in list
#
# my_list =[10, 20, 30 , 40 ,50]
#
# first_elemnt =  my_list[0]
# second_elemnt =  my_list[1]
# print("first Elemet:", first_elemnt)
# print("second Elemet:", second_elemnt)

#  # Q3) Convert str to int
#
# a = "4"
# print(int(a))
# print(type(a))
#
# Q4) Convert a string to a list
#
# str1 = "Faraz Kazi"
# print(str1.split(" "))
#
# Q) function=---
# def add_numbers(number1, number2):
#     result = number1 + number2
#     return result
# sum = add_numbers(5, 9)
# print(sum)

  # Q6) Calculate LEAP YEAR----

# year = int(input("Enter year"))
#
# if (year % 400 == 0) and (year % 4 == 0):
#     print("Its leap year ")
#
# elif (year % 100 == 0):
#     print("Its centeriue year ")
#
# else:
#     print("Its not leap year ")
#
# Q7) ARMSTRONG NUMBER:----

# number = int(input("Enter a number: "))
#
# total = 0
# digits = len(str(number))
#
# for digit in str(number):
#     total = total + int(digit) ** digits
#
# if total == number:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

  # Q8) Reverse the string(Palandrone)

# my_str = input("Enter a string: ")
#
# my_str = my_str.casefold()
#
# print(my_str[::-1])

# my_str = input("Enter a string: ")
# my_str = my_str.casefold()
#
# reversed_str = "".join(reversed(my_str))
#
# if my_str == reversed_str:
#     print("The string is palandroum")
#
# else:
#     print("Not palandroum")
#
# a = 5
# b = 10
# # temp = a
# # a = b
# # temp= b
# # print(a)
#
# a, b = b , a
#
# print(a, b)

 # Q9) Prime Number:----
#
# numebr_usr = int(input('Enter the number: '))
#
# if numebr_usr <= 1:
#     print("Enter a valid number")
#
# else:
#     for i in range(2, numebr_usr):
#         if numebr_usr % i == 0:
#            print("Not prime")
#            break
#
#     else:
#         print("Prime")

# number = int(input("Enter a number: "))
#
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
#
# print("Factorial number is: ", factorial)

import random
from multiprocessing.reduction import duplicate

# num = random.randint(1, 10)
# print(num)
# num1 = random.random()
# print(num1)
# num2 = random.uniform(1, 100)
# print(num2)
# num3 = random.randrange(0, 100, 2)
# print(num3)
# numb4 = random.sample(range(1,10), 3)
# print(numb4)

 # Q11) SQURE ROOT
# number = int(input("Enter a number: "))
#
# square_root = number ** 0.5
#
# print("Square root is:", square_root)
# a =  25
# # b = a **
# import math
#
# number = int(input("Enter number"))
#
# square_root = math.sqrt(number)
#
# print("Square root is: ", square_root)
#  Q) Sawpin the number;--------
# numbers = [10, 20, 30, 40, 50]
#
# numbers[0], numbers[-1] = numbers[-1], numbers[0]
#
# print(numbers)
#
#  Q12) Revers the strin:-----

# name = "Faraz Kazi"
#
# revers_str = name[::-1]
#
# print(revers_str)
#  q13) Sort the list ;----
#
# my_list = [1, 3, 2, 4, 6, 5]
#
# my_list.sort()
#
# print(my_list)

# import os
#
# os.remove("empolyess.csv.py")

 # Q) SQURE LIST
# my_list = [1, 2, 3, 4]
#
# squr_list = [x * x for x in my_list]
# print(squr_list)

 # Q) Split and Join
#
# a = "i am data engineer"
#
# b = a.split(" ")
#
# print(b)
#
#  Q14) Prime number between 100 to 200:----
#
# for number in range(100,201):
#     if number > 1:
#         for i in range (2, number):
#             if number % i == 0:
#                 break
#
#
#         else:
#             print(number)

# for num in range (100, 201):
#     if all(num % i != 0
#            for i in range(2, num)):
#         print(num)

# q) sort list;-

# my_list = [10, 15, 13, 1, 2, 4, 3, 5]
#
# my_list.sort()
#
# print(my_list)
#
# def f (n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# for i in range(1,11):
#     print(f(i))
#
# name = "Faraz kazi"
#
# rev = "".join(reversed(name))
#
# print(rev)
#
#  Q) Extraxt digit;-----

# text = "bac123bfab234bad"
# digit = ""
#
# for char in text:
#     if char.isdigit():
#         digit += char
#
# print(digit)

# list1 = ["My", 'name']
#
# list2 = ["is", 'Faraz']
#
# list3 = " ".join(list1 + list2)
#
# print(list3)

  # Q) Convr list to dict:---
#
# lis1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# # dict = dict(zip(lis1, list))
# #
# # print(dict)
#
# dict = {lis1[i] : list2[i] for i in range(len(lis1))}
#
# print(dict)
#
#  Q) Class clled:----

# class A:
#     count  = 0
#
#     def __init__(self):
#         A.count += 1
#         print("Class clled")
#
# print(A().count)

# count = 0
#
# class A:
#     def __init__(self):
#         global count
#         count += 1
#         print("Class called")
#
# print(count)
#
# a1 = A()
#
# print(count)
#
# text_list = ["Faraz", "Kazi"]
#
# str = ''.join(text_list)
#
# duplicate = []
#
# for chr in str:
#     if str.count(chr) > 1 and chr not in duplicate:
#         duplicate.append(chr)

# for chr in set(str):
#     if str.count(chr) > 1:
#         duplicate.append(chr)
# print(duplicate)
#
# str = "Faraz"
#
# unique = []
#
# for char in str:
#     if str.count(char) == 1 and char not in unique:
#         unique.append(char)
# print(unique)

list =  ["india", "is", "my", "country"]

list2 = [word for word in list
  if word.startswith("i")]
print(list2)