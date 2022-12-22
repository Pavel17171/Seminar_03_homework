# Ex_2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

number = int(input("Введите количество элементов: "))

# Рандомное заполнение списка элементами
list1 = []
for i in range(number):
    list1.append(randint(1, number * 5))
print(f"Список элементов: \n{list1}")

# Заполнение списка произведением пар чисел первого списка
list2 = []
if len(list1) % 2 == 0:
    length_list2 = len(list1) // 2
else:
    length_list2 = len(list1) // 2 + 1       
for i in range(length_list2):
    list2.append(list1[i] * list1[-(i + 1)])
print(f"Список произведения пар чисел: \n{list2}")