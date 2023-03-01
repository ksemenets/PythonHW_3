import random
n = int(input("Введите количество элементов массива"))
list_ = [random.randint(0, 9) for i in range(n)]
x = int(input("Введите число"))
print(list_)
print(list_.count(x))