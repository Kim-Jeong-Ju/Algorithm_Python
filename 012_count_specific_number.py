## 문제 012. 정렬된 배열에서 특정 수의 갯수 구하기

# N개의 원소를 포함한 수열이 오름차순으로 정렬되어 있을 때, 특정 숫자 X가 이 수열에서 등장하는 총 횟수를 계산하는 프로그램을 작성하라
# 단 시간복잡도 제한은 O(logN)으로 알고리즘을 설계해야 한다.

# Input : 첫째 줄에 N과 X가 정수 형태로 공백을 기준으로 입력 (1 <= N <= 1,000,000, -10억 <= X <= 10억)
#         둘째 줄에 N개의 원소가 공백을 기준으로 입력
# Output : 수열에서 값이 X인 원소의 갯수 출력, X가 없다면 -1 출력

from bisect import bisect_left, bisect_right        # 제한된 시간복잡도를 만족하기 위해 라이브러리 사용

n, x = map(int, input().split())
array = list(map(int, input().split()))

left_elem = bisect_left(array, x)
right_elem = bisect_right(array, x)
count = right_elem - left_elem

if count == 0:
    print(-1)
else:
    print(count)