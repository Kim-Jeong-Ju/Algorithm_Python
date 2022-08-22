## 문제 010. 두 배열의 원소 교체

# N개의 원소로 구성된 두 배열 A와 B에 대하여 최대 K번의 두 배열에서의 원소 바꿔치기를 통해 배열 A에 있는 원소의
# 총합이 최대가 되도록 한다. 최대 K번의 바꿔치기를 통해 만들 수 있는 배열 A의 모든 원소의 총합의 최댓값을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 N과 K 입력(1 <= N <= 100,000, 0 <= K <= N)
#         둘째 줄에 배열 A의 원소들이, 셋째 줄에 배열 B의 원소들이 공백을 기준으로 입력
# Output : 배열 A의 모든 원소의 총합의 최댓값

n, k = map(int, input().split())
Array = list(map(int, input().split()))
Brray = list(map(int, input().split()))

Array.sort()                # 배열 A 오름차순으로 정렬
Brray.sort(reverse=True)    # 배열 B 내림차순으로 정렬

for idx in range(k):
    if Array[idx] < Brray[idx]:
        Array[idx], Brray[idx] = Brray[idx], Array[idx]
    else:
        break

print(sum(Array))