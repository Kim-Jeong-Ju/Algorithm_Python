## 문제 104. 통계학 --- 백준 No.2108

import sys
input = sys.stdin.readline

Array = []
N = int(input())
for num in range(N):
    Array.append(int(input()))

def alpha_count(array):
    alpha, beta = dict(), []
    for Anum in array:
        if Anum in alpha.keys(): alpha[Anum] += 1
        else: alpha[Anum] = 1

    max_value = max(alpha.values())
    for Bnum in alpha:
        if max_value == alpha[Bnum]: beta.append(Bnum)

    if len(beta) > 1 : return beta[1]
    else: return beta[0]

Array.sort()

print(round(sum(Array) / N))
print(Array[N // 2])
print(alpha_count(Array))
print(Array[-1] - Array[0])