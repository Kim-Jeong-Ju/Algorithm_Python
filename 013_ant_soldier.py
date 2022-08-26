## 문제 013. 개미 전사

# 개미 전사가 메뚜기 마을의 일직선 상으로 놓인 식량 창고들에 대해 최소한 한 칸 이상 떨어진 식량 창고를 약탈할 수 있다고 할 때,
# 식량 창고 N개에 대해 개미 전사가 약탈할 수 있는 식량의 최댓값을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 식량 창고의 갯수 N 입력 (3 <= N <= 100)
#         둘째 줄에 공백을 기준으로 각 식량 창고에 저장된 식량의 갯수 K 입력 (0 <= K <= 1,000)
# Output : 개미 전사가 약탈 가능한 식량의 최댓값 출력

n = int(input())
foods = list(map(int, input().split()))

dp = [0] * 101      # 특정 i번째 식량 창고까지의 약탈 가능한 식량의 maximum
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for idx in range(2, n):     # 특정 i번째 까지의 maximum = max(특정 i-1번째 까지의 maximum VS 특정 i-2번째 까지의 maximum + i번째 식량)
    dp[idx] = max(dp[idx-1], dp[idx-2] + foods[idx])

print(dp[n-1])