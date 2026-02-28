"""
    # ! 문제 113. 진법 변환 2 --- 백준 No.11005
"""

alpha_crit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

A, B = map(int, input().split())
while A:
    answer += alpha_crit[A % B]
    A //= B

print(answer[::-1])