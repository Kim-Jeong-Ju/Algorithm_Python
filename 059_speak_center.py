## 문제 059. 가운데를 말해요 --- 백준 No.1655

import sys
import heapq

N = int(sys.stdin.readline())
left_heap, right_heap, array = [], [], []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap): heapq.heappush(left_heap, -num)
    else: heapq.heappush(right_heap, num)

    if right_heap and right_heap[0] < -left_heap[0]:
        min_left = heapq.heappop(left_heap)
        min_right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -min_right)
        heapq.heappush(right_heap, -min_left)

    array.append(-left_heap[0])

for num in array: print(num)