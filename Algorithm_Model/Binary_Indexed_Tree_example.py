## Binary Indexed Tree(Fenwick Tree) Algorithm Example Code -- 이해 필요
## 2진법 Index 구조를 활용해 구간합에 대한 문제를 효과적으로 해결하는 자료구조 -> 시간복잡도 제한이 심할때 유용 -> 최악의 경우에도 O(logN) 보장

# 수시로 변하는 N개의 수에 대해 구간합을 구하는 프로그램을 작성하라.
# 단, 데이터의 갯수 1 <= N <= 1,000,000, 데이터의 변경 횟수 1 <= M <= 10,000, 구간합 계산 횟수 1 <= K <= 10,000

n, m, k = map(int, input().split())

array = [0] * (n + 1)        # 각각의 숫자에 대해 그 숫자가 포함하는 숫자들의 갯수
tree = [0] * (n + 1)         # Binary Indexed Tree 결과를 저장하는 table

def prefix_sum(index):
    result = 0
    while index > 0:
        result += tree[index]           # 누적합 계산
        index -= index & (-index)       # 0이 아닌 마지막 bit의 수만큼 빼면서 이동

    return result

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(end - 1)

def value_update(index, diff):
    while index <= n:
        tree[index] += diff             # 변경되는 숫자와 변경되기 이전 숫자의 차이만큼 합 계산
        index += index & (-index)       # 0이 아닌 마지막 bit의 수만큼 더하면서 이동

for idx in range(1, n + 1):
    num = int(input())
    array[idx] = num
    value_update(idx, num)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        value_update(b, c - array[b])
        array[b] = c
    else:
        print(interval_sum(b, c))