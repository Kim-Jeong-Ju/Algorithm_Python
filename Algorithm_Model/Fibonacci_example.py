## Fibonacci Function Algorithm Example Code

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

print(dp_topdown_fibo(6))

dp1 = [0] * 100
def validate_topdown_fibo(num):
    print('f(' + str(num) + ')', end=" ")
    if num == 1 or num == 2:
        return 1
    else:
        if dp1[num] != 0:
            return dp1[num]
        else:
            dp1[num] = validate_topdown_fibo(num-1) + validate_topdown_fibo(num-2)
            return dp1[num]

validate_topdown_fibo(6)
print()




dp2 = [0] * 100                # Bottom-Up(DP)를 통한 피보나치 수열 구현
dp2[1] = 1
dp2[2] = 1
num = 6

for i in range(3, num + 1):
    dp2[i] = dp2[i-1] + dp2[i-2]

print(dp2[num])