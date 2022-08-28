## Min Heap and Max Heap Algorithm Example Code

import heapq

def AscHeapSort(array):                         # 오름차순 힙 정렬 : Min Heap 사용
    heap = []
    result = []

    for elem in array:
        heapq.heappush(heap, elem)

    for _ in range(len(heap)):
        result.append(heapq.heappop(heap))

    return result

def DescHeapSort(array):                        # 내림차순 힙 정렬 : Max Heap 사용
    heap = []
    result = []

    for elem in array:
        heapq.heappush(heap, -elem)

    for _ in range(len(heap)):
        result.append(-heapq.heappop(heap))

    return result

array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(f"Ascending Sort by Min Heap : {AscHeapSort(array)}")
print(f"Descending Sort by Min Heap : {DescHeapSort(array)}")