## 문제 072. 징검다리 건너기 --- 프로그래머스 Lv.3 연습 문제

def solution(stones, k):
    answer = 0

    left, right = 1, max(stones)
    while left <= right:
        count, mid = 0, (left + right) // 2
        for stone in stones:
            if stone - mid <= 0:
                count += 1  # 연속으로 나오면 +1
            else:
                count = 0  # 연속이 아니면 0으로 초기화

            if count >= k: break

        if count < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer