#Write a program that reads the lengths of two legs in a right triangle and outputs its area.
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

a, b = float(input()), float(input())
S = 1 / 2 * a * b
print(S)

# Two old ladies are walking towards each other at constant speeds of V and V km/h. Determine after what time the old ladies will meet,
# if the distance between them is SS km.
# Две старушки идут навстречу друг другу с постоянными скоростями V и V км/ч. Определите, через какое время старушки встретятся,
# если расстояние между ними равно SS км.

S, V1, V2 = float(input()), float(input()), float(input())
V = V1 + V2
t = S / V
print(t)
