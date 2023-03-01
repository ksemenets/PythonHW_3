import random
n = int(input("Введите количество элементов массива"))
list_ = [random.randint(0, 9) for i in range(n)]
x = int(input("Введите число"))
print(list_)
y = abs(x-list_[0])
c = 0
for i in range(n-1):
    if abs(x - list_[i]) < y:
        y = abs(x-list_[i])
        c = list_[i]
print(c)