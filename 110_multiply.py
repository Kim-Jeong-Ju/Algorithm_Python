"""
    # ! 문제 110. 곱셈 --- 백준 No.1629
"""

import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

def adjust_multi(A_val, B_val, mod):
    if B_val == 1:  return A_val % mod
    else:
        temp = adjust_multi(A_val, B_val // 2, mod)
        if B_val % 2 == 0:  return (temp * temp) % mod
        else:               return (A_val * temp * temp) % mod

print(adjust_multi(A, B, C))