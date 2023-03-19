## 문제 046. 파괴되지 않은 건물 --- 프로그래머스 Lv.3 연습 문제

def solution(board, skills):
    answer = 0

    array = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for skill in skills:
        type, r1, c1, r2, c2, degree = map(int, skill)
        array[r1][c1] += degree if type == 2 else -degree
        array[r2 + 1][c2 + 1] += degree if type == 2 else -degree
        array[r1][c2 + 1] += -degree if type == 2 else degree
        array[r2 + 1][c1] += -degree if type == 2 else degree

    for a in range(len(array) - 1):
        for b in range(len(array[0]) - 1):
            array[a][b + 1] += array[a][b]

    for c in range(len(array[0]) - 1):
        for d in range(len(array) - 1):
            array[d + 1][c] += array[d][c]

    for e in range(len(board)):
        for f in range(len(board[e])):
            board[e][f] += array[e][f]
            if board[e][f] > 0: answer += 1

    return answer