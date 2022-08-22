## 문제 003. 모험가 길드 -- 이해 필요

# N명의 모험가에 대하여 공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가 길드에 있어야 함.
# 각각의 공포도를 갖는 N명의 모험가에 대해 구성할 수 있는 길드 수의 최댓값을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 모험가의 수 N(1 <= N <= 100,000), 둘째 줄에 각 모험가의 공포도 X(1 <= X <= N)
# Output : 구성 가능한 길드 수의 최댓값

## 정답 풀이 -- 이해/수정 필요
adventures = int(input())
fears = list(map(int, input().split()))
fears.sort()        # 공포도 오름차순 정렬

guild_cnt = 0       # 총 길드의 수
advt_cnt = 0        # 현재 길드에 소속된 모험가의 수

for fear in fears:      # 모험가 각각의 공포도를 확인하며 반복
    advt_cnt += 1       # 현재 확인중인 모험가를 길드에 추가

    if advt_cnt >= fear:    # 현재 확인중인 길드 내 모험가 수 >= 현재 확인중인 모험가의 공포도
        guild_cnt += 1      # 길드 수 증가
        advt_cnt = 0        # 현재 확인중인 길드 내 모험가 수 = 0으로 초기화

print(guild_cnt)