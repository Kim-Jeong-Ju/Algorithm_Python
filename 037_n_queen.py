## 문제 037. N-Queen --- 프로그래머스 Lv.2 연습 문제

def n_queen(n, row, cols):
    count = 0

    if row == n: return 1
    for a in range(n):
        cols[row] = a
        if check(row, cols):
            count += n_queen(n, row + 1, cols)

    return count


def check(row, cols):
    for b in range(row):
        if cols[row] == cols[b] or row - b == abs(cols[row] - cols[b]):
            return False
    return True


def solution(n):
    answer = n_queen(n, 0, [0] * n)

    return answer