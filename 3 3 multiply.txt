a = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]
b = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):  # Adjusted for the new matrix size
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for row in c:
    print(row)
