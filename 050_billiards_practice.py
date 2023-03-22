## 문제 050. 당구 연습 --- 프로그래머스 Lv.2 연습 문제

def solution(m, n, startX, startY, balls):
    answer = []

    for ballX, ballY in balls:
        pass_idx = -1
        if startX == ballX and startY > ballY:
            pass_idx = 3
        elif startX == ballX and startY < ballY:
            pass_idx = 2
        elif startY == ballY and startX > ballX:
            pass_idx = 0
        elif startY == ballY and startX < ballX:
            pass_idx = 1

        # left / right / up / down 순서
        symms = [[-startX, startY], [(2 * m) - startX, startY], [startX, (2 * n) - startY], [startX, -startY]]
        dists = []
        for a, symm in enumerate(symms):
            if a == pass_idx:
                continue

            dist = ((symm[0] - ballX) ** 2) + ((symm[1] - ballY) ** 2)
            dists.append(dist)

        answer.append(min(dists))

    return answer