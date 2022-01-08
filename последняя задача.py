from random import choice
import numpy as np
n = int(input('Pls input integer number > 2: '))
mtx = []
if n <= 2:
    print('Read instruction one more time ')
else:
    for i in range(n):
        mtx1 = np.array([choice([-1, 1]) for i in range(n)])
        print(mtx1)
        mtx.append(np.array(mtx1))
    sum = 0
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += (mtx[i][n - 1]) * (mtx[i][0])
        for j in range(n - 1):
            sum1 += (mtx[i][j] * (mtx[i][j + 1]))
    for j in range(n):
        sum2 += (mtx[n - 1][j]) * (mtx[0][j])
        for i in range(n - 1):
            sum2 += (mtx[i][j] * (mtx[i + 1][j]))
    sum = sum1 + sum2
    print()
    print(sum)