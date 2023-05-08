## 문제 073. 두 큐 합 같게 만들기 --- 프로그래머스 Lv.2 연습 문제

from collections import deque

def solution(queue1, queue2):
    answer = 0

    max_iter = len(queue1) * 3
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_diff = sum(queue1) - sum(queue2)

    if sum_diff == 0:
        pass
    else:
        while sum_diff > 0 or sum_diff < 0:
            if answer >= max_iter:
                answer = -1
                break

            if sum_diff > 0:  # queue1 총합이 더 크면
                move = queue1.popleft()
                queue2.append(move)
                sum_diff -= move * 2
            elif sum_diff < 0:  # queue2 총합이 더 크면
                move = queue2.popleft()
                queue1.append(move)
                sum_diff += move * 2

            answer += 1

    return answer