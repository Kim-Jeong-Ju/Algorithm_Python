## 문제 030. Flatten --- SWEA 1208번 문제

def find_idx(array):
    maxi, max_idx = 1, 0
    mini, min_idx = 100, 0
    for idx, value in enumerate(array):
        if maxi < value:
            maxi = value
            max_idx = idx

        if mini > value:
            mini = value
            min_idx = idx

    return max_idx, min_idx


T = 10
for test_case in range(1, T+1):
    dump_num = int(input())
    boxes = list(map(int, input().split()))
    diff = 0

    while dump_num > 0:
        max_idx, min_idx = find_idx(boxes)
        diff = boxes[max_idx] - boxes[min_idx]

        if diff <= 1:
            break

        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        dump_num -= 1

    print(f"#{test_case} {diff}")