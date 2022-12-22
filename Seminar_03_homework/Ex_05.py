# Ex_5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

number = int(input("Введите число: "))
list_fib = []
list_negfib = []
for i in range(number + 1):
    if i < 2:
        list_fib.append(i)
        list_negfib.append(((-1)**(i+1))*i)
    else:
        temp = list_fib[i - 1] + list_fib[i - 2]
        list_fib.append(temp)
        list_negfib.append((-1) ** (i + 1) * temp)        
list_negfib = list_negfib[:0:-1] + list_fib
print(list_negfib)