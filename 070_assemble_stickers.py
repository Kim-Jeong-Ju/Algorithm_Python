## 문제 070. 스티커 모으기(2) --- 프로그래머스 Lv.3 연습 문제

def solution(sticker):
    answer = 0
    size = len(sticker)

    if size == 1:
        answer = sticker[0]
    else:
        dp1 = [0 for _ in range(size)]              # 0-index부터 스티커 사용
        dp1[0], dp1[1] = sticker[0], sticker[0]
        dp2 = [0 for _ in range(size)]              # 1-index부터 스티커 사용
        dp2[1] = sticker[1]

        for a in range(2, size - 1):        # 마지막 스티커 사용 X
            dp1[a] = max(dp1[a - 1], dp1[a - 2] + sticker[a])

        for b in range(2, size):            # 마지막 스티커 사용 O
            dp2[b] = max(dp2[b - 1], dp2[b - 2] + sticker[b])

        answer = max(dp1[size - 2], dp2[size - 1])

    return answer