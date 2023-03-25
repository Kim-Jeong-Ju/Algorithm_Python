## 문제 052. 야근 지수 --- 프로그래머스 Lv.3 연습 문제

import heapq


def solution(n, works):
    answer = 0
    heap = []

    for val in works:
        heapq.heappush(heap, -val)
    for _ in range(n):
        max_val = -heapq.heappop(heap)
        if max_val == 0:
            break
        else:
            heapq.heappush(heap, -(max_val - 1))

    heap = [num ** 2 for num in heap]
    answer = sum(heap)

    return answer