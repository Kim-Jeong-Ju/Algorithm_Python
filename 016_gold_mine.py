## 문제 016. 금광

# N X M 크기의 금광에 대해 첫번째 열의 임의의 행에서 시작하여 오른쪽으로 1열씩 이동하며 금을 채취한다. 이동 시에는
# 오른쪽 위, 오른쪽, 오른쪽 아래 총 3가지 경우로 이동이 가능하다고 할 때, 채취할 수 있는 금의 최댓값을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 테스트 케이스(프로그램 시행 횟수) T 입력 (1 <= T <= 1,000)
#         이후 매 테스트 케이스의 첫째 줄에 N과 M이 공백 기준으로 입력(1 <= N, M <= 20)
#         매 테스트 케이스의 둘째 줄에 N X M 금광의 각 칸마다 존재하는 금의 양 입력 (1 <= 각 칸의 금의 양 <= 100)
# Output : 테스트 케이스마다 채굴 가능한 금의 최대값을 줄바꿈하여 출력

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))

    dp = []             # DP table은 이제까지 지나쳐오며 채굴한 금의 maximum값으로 매번 update
    idx = 0
    for _ in range(n):
        dp.append(golds[idx:idx+m])
        idx += m

    for a in range(1, m):                   # 금광 행렬의 모든 열에 대하여
        for b in range(n):                  # 금광 행렬의 특정 열 내의 모든 행에 대하여
            if b == 0:                      # 금광 행렬의 1번째 행
                left_up = 0
            else:
                left_up = dp[b-1][a-1]      # 왼쪽 위에서부터 오는 경우
            if b == n-1:                    # 금광 행렬의 N번째 행
                left_down = 0
            else:
                left_down = dp[b+1][a-1]    # 왼쪽 아래에서부터 오는 경우
            left = dp[b][a-1]               # 왼쪽에서부터 오는 경우
            dp[b][a] = dp[b][a] + max(left_up, left, left_down)     # DP table에 maximum 누적합으로 갱신

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][m-1])    # 제일 마지막 열에 대해 각 행을 모두 확인하며 max값 찾기
    print(max_gold)