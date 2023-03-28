## 문제 054. 네트워크 --- 프로그래머스 Lv.3 연습 문제

def solution(m, n, puddles):
    answer = 0
    array = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        if [1, row + 1] in puddles:
            break
        else:
            array[row][0] = 1
    for col in range(m):
        if [col + 1, 1] in puddles:
            break
        else:
            array[0][col] = 1

    for a in range(1, n):
        for b in range(1, m):
            if [b + 1, a + 1] in puddles:
                continue

            if a == 0:
                array[a][b] = 1
            else:
                if b == 0:
                    array[a][b] += array[a - 1][b]
                else:
                    array[a][b] += (array[a - 1][b] + array[a][b - 1])

    answer = array[-1][-1] % 1000000007
    return answer