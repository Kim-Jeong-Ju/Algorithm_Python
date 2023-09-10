## 문제 096. 어린 왕자 --- 백준 No.1004

T = int(input())

for _ in range(T):
    a1, b1, a2, b2 = map(int, input().split())
    count = 0

    n = int(input())
    array = [0] * n
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_dist = (a1 - cx) ** 2 + (b1 - cy) ** 2
        end_dist = (a2 - cx) ** 2 + (b2 - cy) ** 2
        crit = r ** 2

        if start_dist > crit and end_dist < crit: count += 1
        if start_dist < crit and end_dist > crit: count += 1

    print(count)