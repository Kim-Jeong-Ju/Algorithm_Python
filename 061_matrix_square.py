## 문제 061. 행렬 제곱 --- 백준 No.10830

import sys
input = sys.stdin.readline

def mat_mul(Array, Brray, N, p):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                result[a][b] += Array[a][c] * Brray[c][b]
            result[a][b] %= p

    return result


def square(matrix, num, N, p):
    if num == 1:
        for row in range(N):
            for col in range(N):
                matrix[row][col] %= p
        return matrix
    elif num == 2:
        return mat_mul(matrix, matrix, N, p)
    else:
        temp = square(matrix, num // 2, N, p)
        if num % 2 == 1:
            return mat_mul(mat_mul(temp, temp, N, p), matrix, N, p)
        else:
            return mat_mul(temp, temp, N, p)


N, B = map(int, input().split())
p = 1000
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

answer = square(array, B, N, p)
for each_row in answer:
    print(*each_row)