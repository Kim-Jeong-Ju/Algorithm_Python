## 문제 021. 피보나치 함수 --- 백준 No.1003

T = int(input())

dp = [(0, 0) for _ in range(41)]
dp[0] = (1, 0)
dp[1] = (0, 1)
dp[2] = (1, 1)

def fibonacci_with_dp(num, dp):
    if num == 0:
        return dp[0][0], dp[0][1]

    elif num == 1:
        return dp[1][0], dp[1][1]

    else:
        if dp[num-1] == (0, 0) and dp[num-2] == (0, 0):
            zero_cnt1, one_cnt1 = fibonacci_with_dp(num-1, dp)
            zero_cnt2, one_cnt2 = fibonacci_with_dp(num-2, dp)
            dp[num] = (zero_cnt1 + zero_cnt2, one_cnt1 + one_cnt2)

        elif dp[num-1] != (0, 0) and dp[num-2] == (0, 0):
            zero_cnt1, one_cnt1 = dp[num-1][0], dp[num-1][1]
            zero_cnt2, one_cnt2 = fibonacci_with_dp(num - 2, dp)
            dp[num] = (zero_cnt1 + zero_cnt2, one_cnt1 + one_cnt2)

        elif dp[num-1] == (0, 0) and dp[num-2] != (0, 0):
            zero_cnt1, one_cnt1 = fibonacci_with_dp(num - 1, dp)
            zero_cnt2, one_cnt2 = dp[num-2][0], dp[num-2][1]
            dp[num] = (zero_cnt1 + zero_cnt2, one_cnt1 + one_cnt2)

        else:
            zero_cnt1, one_cnt1 = dp[num-1][0], dp[num-1][1]
            zero_cnt2, one_cnt2 = dp[num-2][0], dp[num-2][1]
            dp[num] = (zero_cnt1 + zero_cnt2, one_cnt1 + one_cnt2)

        return dp[num][0], dp[num][1]

for _ in range(T):
    n = int(input())
    zero_cnt, one_cnt = fibonacci_with_dp(n, dp)
    print(zero_cnt, one_cnt)