# Ex_4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число: "))
number2 = str(number % 2)
while (number >= 2):
    number //= 2
    number2 += str(number % 2)
number2 = int(number2[::-1])
print(number2)