## 문제 001. 1이 될 때까지

# 1 <= N <= 100,000인 N에 대하여 (N-1) 혹은 (N/K, 단 K로 나누어 떨어질 때만)를 반복적으로 수행해
# N=1이 될 때까지의 최소 연산 횟수를 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 N과 K가 공백을 기준으로 각각 자연수 입력
# Output : 수행해야 하는 연산의 총 횟수

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:      # N이 K로 나누어 떨어지면 나누기 연산
        n //= k
        count += 1
    else:               # 나누어 떨어지지 않으면 -1 연산
        n -= 1
        count += 1

print(count)