## 문제 083. 순위 --- 프로그래머스 Lv.3 연습 문제

def solution(n, results):
    answer = 0
    check = [0 for _ in range(n)]
    array = [[0 for _ in range(n)] for _ in range(n)]

    for winner, loser in results:
        array[winner - 1][loser - 1] = 1

    for k in range(n):
        for a in range(n):
            for b in range(n):
                if array[a][b] == 0 and (array[a][k] == 1 and array[k][b] == 1):
                    array[a][b] = 1

    for a in range(n):
        for b in range(n):
            if array[a][b] == 1:
                check[a] += 1
                check[b] += 1

    answer = sum([1 for num in check if num == n - 1])
    return answer