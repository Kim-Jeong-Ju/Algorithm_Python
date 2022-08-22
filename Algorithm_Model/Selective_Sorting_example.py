## Selective Sorting Algorithm Example Code

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for a in range(len(array)):
    min_idx = a     # 첫번째 원소부터 증가하며 최소 index로 설정

    for b in range(a + 1, len(array)):      # min_idx 보다 이후에 나오는 모든 원소들에 대해
        if array[min_idx] > array[b]:       # min_idx의 값보다 이후에 나오는 것 중에 작은 것이 있으면
            min_idx = b                     # min_idx 갱신

    array[min_idx], array[a] = array[a], array[min_idx]     # swap

print(array)