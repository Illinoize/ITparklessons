graph = [[0, 1, 0, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0]]


def check_loop(graph):
    for i in graph:
        for j in graph[i]:
            if j == i and graph[i][j] == 1:
                print('В графе есть петли')
            else:
                print('В графе нет петли')


check_loop(graph=graph)


