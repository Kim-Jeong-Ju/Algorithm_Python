## 문제 089. 디펜스 게임 --- 프로그래머스 Lv.2 연습 문제

import heapq

def solution(n, k, enemy):
    answer = 0

    heap = []
    for idx, num in enumerate(enemy):
        heapq.heappush(heap, num)
        if len(heap) > k:
            n -= heapq.heappop(heap)
        if n < 0:
            return idx

    answer = len(enemy)
    return answer