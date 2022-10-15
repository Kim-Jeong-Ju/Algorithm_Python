## Two Pointers Algorithm Example Code
## list에 순차적으로 접근 시 시작점, 끝점을 기준으로 위치를 기록하며 처리하는 알고리즘

# N개의 자연수로 구성된 수열에 대하여 합이 M인 부분 연속 수열의 갯수를 구하는 프로그램을 작성하라.
# 수행 제한 시간 : O(N)

n, m = map(int, input().split())
array = list(map(int, input().split()))

start_idx = 0
end_idx = 0
count = 0

while start_idx <= n and end_idx <= n:
    summation = sum(array[start_idx:end_idx])
    if summation < m:
        end_idx += 1
    if summation == m:
        count += 1
        start_idx += 1
    if summation > m:
        start_idx += 1

print(count)




## N개의 자연수로 구성된 수열에 대하여 left_index, right_index 쿼리가 주어질 때, 주어진 구간 내의 합을 구하는 프로그램을 작성하라.

n, left_idx, right_idx = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = sum(array[0:i + 1])

print(prefix_sum[right_idx] - prefix_sum[left_idx - 1])