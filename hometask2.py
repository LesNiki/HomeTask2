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

# num=input("Введите число: ")
# sum=0
# for digit in num:
#     if digit.isdigit():
#         sum+=int(digit)
# print(sum)

# Задача: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num=int(input("Введите число: "))
comp=1
list=[]
i=2
while i<=num+1:
    list.append(comp)
    comp*=i
    i+=1
print(list)


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
