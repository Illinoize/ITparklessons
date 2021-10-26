matrix = [[[i for i in range(2, 7)] for j in range(7)] for k in range(3)]

for k in range(3):
    for i in range(7):
        for j in range(5):
            print(matrix[k][i][j], end=' ')
        print()
    print()