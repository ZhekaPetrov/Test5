# Write a program that reads two integers and a string from the keyboard. If this string is the notation of one of the four mathematical
# operations (+, -, *, /), then output the result of applying this operation to the previously entered numbers, otherwise output "Invalid
# operation". If the user wants to divide by zero, print the text "You can't divide by zero!".

# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх
# математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае
# выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

a, b, c = int(input()), int(input()), input()
if b == 0 and c =="/":
    print("На ноль делить нельзя!")
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("Неверная операция")

