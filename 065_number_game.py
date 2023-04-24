## 문제 065. 숫자 게임 --- 프로그래머스 Lv.3 연습 문제

from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    A_queue = deque(A)
    B_queue = deque(B)
    while B_queue:
        if A_queue[0] < B_queue[0]:
            A_queue.popleft()
            B_queue.popleft()
            answer += 1
        else:
            B_queue.popleft()

    return answer