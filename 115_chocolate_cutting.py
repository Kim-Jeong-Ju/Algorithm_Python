"""
    # ! 문제 115. 초콜릿 자르기 --- 백준 No.2163
"""

import queue

A, B = map(str, input().split())
answer = 0

queue = queue.Queue()
queue.put(A + "X" + B)

while queue.qsize() > 0:
    A_len, B_len = map(int, queue.get().split("X"))

    if A_len == B_len == 1: pass
    else:
        if A_len >= B_len:
            AA_len = A_len // 2
            A_len -= AA_len
            
            answer += 1

            if A_len > 1 or B_len > 1:  queue.put(str(A_len) + "X" + str(B_len))
            if AA_len > 1 or B_len > 1: queue.put(str(AA_len) + "X" + str(B_len))

        else:
            BB_len = B_len // 2
            B_len -= BB_len

            answer += 1

            if A_len > 1 or B_len > 1:  queue.put(str(A_len) + "X" + str(B_len))
            if A_len > 1 or BB_len > 1: queue.put(str(A_len) + "X" + str(BB_len))

print(answer)