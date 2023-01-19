# Write a program that reads the pocket number and shows whether this pocket is green, red or black. The program should display an error
# message if the user enters a number that lies outside the range from 0 to 36.

# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна
# вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

a = int(input())
if 0 > a or a > 36:
    print("ошибка ввода")
elif a == 0:
    print("зеленый")
elif 1 <= a <= 10:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= a <= 18:
    if a % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 19 <= a <= 28:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= a <= 36:
    if a % 2 == 0:
        print("красный")
    else:
        print("черный")
