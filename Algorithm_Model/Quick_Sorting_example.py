## Quick Sorting Algorithm Example Code

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]        # pivot을 list의 첫번째 원소로 설정
    rest = array[1:]        # pivot을 제외한 나머지 원소들끼리 list로 묶음

    left_side = [a for a in rest if a <= pivot]     # pivot보다 작은 원소들끼리의 group
    right_side = [b for b in rest if b > pivot]     # pivot보다 큰 원소들끼리의 group

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)     # 재귀적으로 left & right에 quick_sort 호출

print(quick_sort(array))