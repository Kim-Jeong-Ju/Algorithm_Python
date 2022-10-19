## Binary Search Algorithm Example Code

from bisect import bisect_left, bisect_right    # 이진 탐색 라이브러리

n, target = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def bisect_recursive(array, target, start, end):     # 재귀 호출을 이용한 이진 탐색 구현
    if start > end:
        return None

    mid = (start + end) // 2        # 중간점 = (시작점 + 끝점) / 2 값의 소수점 버림

    if array[mid] == target:        # 중간점 = 찾는값이면, 정답 출력
        return mid
    elif array[mid] > target:       # 중간점 > 찾는값이면, 끝점 = 중간점 - 1로 갱신 후 재귀 호출
        return bisect_recursive(array, target, start, mid - 1)
    else:                           # 중간점 < 찾는값이면, 시작점 = 중간점 + 1로 갱신 후 재귀 호출
        return bisect_recursive(array, target, mid + 1, end)

def bisect_iteration(array, target, start, end):        # 반복문을 이용한 이진 탐색 구현
    while start <= end:
        mid = (start + end) // 2        # 중간점 = (시작점 + 끝점) / 2 값의 소수점 버림

        if array[mid] == target:        # 중간점 = 찾는값이면, 정답 출력
            return mid
        elif array[mid] > target:       # 중간점 > 찾는값이면, 끝점 = 중간점 - 1로 갱신 후 반복
            end = mid - 1
        else:                           # 중간점 < 찾는값이면, 시작점 = 중간점 + 1로 갱신 후 반복
            start = mid + 1

    return None

result1 = bisect_recursive(array, target, 0, n - 1)
result2 = bisect_iteration(array, target, 0, n - 1)
print(array)
print()

if result1 == None:
    print("원소가 존재하지 않습니다.")
else:
    print(f"{result1}-index에 찾는 원소가 존재합니다.")

if result2 == None:
    print("원소가 존재하지 않습니다.")
else:
    print(f"{result2}-index에 찾는 원소가 존재합니다.")

print()




print(bisect_left(array, target))
print(bisect_right(array, target))