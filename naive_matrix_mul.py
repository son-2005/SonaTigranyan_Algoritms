def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Չի կարելի բազմապատկել՝ չափերը չեն համապատասխանում։")
        return None

    result = []
    for i in range(rows_A):
        row = [0] * cols_B
        result.append(row)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result
#Օրինակ
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result = multiply_matrices(A, B)

print("Արդյունքը:")
for row in result:
    print(row)
