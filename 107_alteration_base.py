"""
    # ! 문제 107. 진법 변환 --- 백준 No.2745
"""

alpha_crit = {'A': 10, 'B': 11, "C": 12, 'D': 13, 'E': 14, 'F': 15,
              'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22,
              'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28,
              'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

A_num, B_num = input().split()
A_num = A_num[::-1]
B_num = int(B_num)

answer = 0

for idx in range(len(A_num)):
    if A_num[idx].isalpha(): answer += alpha_crit[A_num[idx]] * (B_num ** idx)
    else: answer += int(A_num[idx]) * (B_num ** idx)

print(answer)