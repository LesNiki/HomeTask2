# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23      - 0,56 -> 11

# num=input("Введите число: ")
# list = []
# i = 0
# sum=0
# for char in num:
#     if char == "." or char == "," or char == "-":
#         char = 0
#     list.append(int(char))
#     sum = sum + list[i]
#     i+=1
# print(sum)

# альтернативное решение:
# num=input("Введите число: ")
# sum=0
# for digit in num:
#     if digit.isdigit():
#         sum+=int(digit)
# print(sum)

# Задача: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num=int(input("Введите число: "))
# comp=1
# list=[]
# i=2
# while i<=num+1:
#     list.append(comp)
#     comp*=i
#     i+=1
# print(list)


# Задайте список из n чисел последовательности $(1+1/n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num=int(input("Введите число: "))
# numdict=dict()
# for n in range(1, num+1):
#     numdict[n]=round((1+1/n)**n,2)
# print(numdict)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint

# n=int(input("Введите число: "))
# file_path="seminar_2/file.txt"
# #добавление в файл позиций, исходя из n
# with open(file_path, "w") as write_file:
#     for i in range(randint(1,n)):
#         write_file.write(f"{randint(0,n-1)}\n)")
# #создание списка:
# nums=[]
# for i in range(n):
#     nums.append(randint(-n,n))
# #считывание позиций:
# with open(file_path) as read_file:
#     positions=read_file.read().split("\n")
# #высчитывание произведения:
# prod_nums=0
# for index in positions:
#     prod_nums*=nums[index]
# print(prod_nums)

# Задача: Реализуйте алгоритм перемешивания списка.

import random
nums=list(range(5))
print(nums)
random.shuffle(nums)
print(nums)