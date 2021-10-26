import random

n = int(input('Введите число n: '))
m = int(input('Введите число m: '))

matrix = [[random.randint(-50, 50) for i in range(n)] for j in range(m)]
positive = 0
negative = 0


for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
        if matrix[i][j] >= 0:
            positive += 1
        else:
            negative += 1
    print()
print('Положительных чисел:', positive, 'Отрицательных чисел:', negative)



