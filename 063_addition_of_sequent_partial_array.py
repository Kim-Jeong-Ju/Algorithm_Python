## 문제 063. 연속된 부분 수열의 합 --- 프로그래머스 Lv.2 연습 문제

def solution(sequence, k):
    answer = []

    start_idx, end_idx, size = 0, 0, len(sequence)
    prefix_sum = [0 for _ in range(size)]
    for idx in range(size):
        if idx == 0:
            prefix_sum[idx] = sequence[idx]
        else:
            prefix_sum[idx] = prefix_sum[idx - 1] + sequence[idx]

    while start_idx < size and end_idx < size:
        if start_idx == 0 and end_idx != 0:
            addition = prefix_sum[end_idx]
        elif start_idx == end_idx:
            addition = sequence[start_idx]
        else:
            addition = prefix_sum[end_idx] - prefix_sum[start_idx - 1]

        if addition < k:
            end_idx += 1
        elif addition == k:
            answer.append([start_idx, end_idx])
            start_idx += 1
        else:
            start_idx += 1

    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))[0]
    return answer