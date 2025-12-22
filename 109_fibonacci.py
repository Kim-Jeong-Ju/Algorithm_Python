"""
    # ! 문제 109. 피보나치 --- 백준 No.2747
"""

dp = [0] * 100
def dp_topdown_fibo(num):      # Top-Down Memoization(DP)을 통한 피보나치 수열 구현 -> 시간복잡도 = O(N)
    if num == 1 or num == 2:
        return 1
    else:
        if dp[num] != 0:
            return dp[num]
        else:
            dp[num] = dp_topdown_fibo(num-1) + dp_topdown_fibo(num-2)
            return dp[num]

num = int(input())
print(dp_topdown_fibo(num))