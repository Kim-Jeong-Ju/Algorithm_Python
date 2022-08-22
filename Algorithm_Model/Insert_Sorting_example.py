## Insert Sorting Algorithm Example Code

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for a in range(1, len(array)):      # 첫번째 원소는 고정 후 나머지 원소들에 대해
    for b in range(a, 0, -1):       # 현재 확인하고 있는 원소보다 index가 작은 모든 원소들에 대해
        if array[b] < array[b-1]:       # "현재 확인하는(idx) 원소의 값 < 인덱스가 하나 작은(idx - 1) 원소의 값" 이면
            array[b], array[b-1] = array[b-1], array[b]     # swap
        else:
            break       # 아니면 반복 실행 멈춤

print(array)