## 문제 079. 경주로 건설 --- 프로그래머스 Lv.3 연습 문제

INF = int(1e9)
from collections import deque

def solution(board):
    answer, size = 0, len(board)
    array = [[[INF for _ in range(size)] for _ in range(size)] for _ in range(4)]
    da, db = [0, -1, 1, 0], [-1, 0, 0, 1]  # Left, Up, Down, Right 순서
    queue = deque([])

    for direct in range(4):  # 방향별 array 초기화
        array[direct][0][0] = 0
        if direct == 2 and board[1][0] == 0:  # Down
            array[direct][1][0] = 100
            queue.append([1, 0, direct, 100])
        elif direct == 3 and board[0][1] == 0:  # Right
            array[direct][0][1] = 100
            queue.append([0, 1, direct, 100])

    while queue:
        a, b, before_dir, before_cost = queue.popleft()
        for after_dir in range(4):
            aa = a + da[after_dir]
            bb = b + db[after_dir]
            if 0 <= aa < size and 0 <= bb < size and board[aa][bb] != 1:
                after_cost = before_cost + (100 if before_dir == after_dir else 600)
                if array[after_dir][aa][bb] > after_cost:
                    array[after_dir][aa][bb] = after_cost
                    queue.append([aa, bb, after_dir, after_cost])

    answer = min([array[direct][-1][-1] for direct in range(4)])
    return answer