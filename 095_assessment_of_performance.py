## 문제 095. 인사고과 --- 프로그래머스 Lv.3 연습 문제

from itertools import combinations

def solution(scores):


    ## 시간 초과 O 풀이
    # answer = 0
    #
    # temp1 = [[idx, score1, score2] for idx, (score1, score2) in enumerate(scores)]
    # for A_info, B_info in combinations(temp1, 2):
    #     if A_info in temp1 and B_info in temp1:
    #         if A_info[1] < B_info[1] and A_info[2] < B_info[2]:
    #             if A_info[0] == 0: return -1
    #             else: del temp1[temp1.index(A_info)]
    #         elif A_info[1] > B_info[1] and A_info[2] > B_info[2]:
    #             if B_info[0] == 0: return -1
    #             else: del temp1[temp1.index(B_info)]
    #
    # temp2 = sorted(temp1, reverse=True, key=lambda x: sum(x)-x[0])
    # addition = 0
    # for seq, (idx, score1, score2) in enumerate(temp2):
    #     if seq == 0:
    #         addition = score1 + score2
    #         answer += 1
    #     else:
    #         if addition == score1 + score2: pass
    #         else:
    #             addition = score1 + score2
    #             answer = seq + 1
    #
    #     if idx == 0: return answer


    ## 시간 초과 X 풀이
    ## 정답 풀이 -- 이해 필요
    answer = 1
    wanho, wanho_sum = scores[0], sum(scores[0])
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))

    thres = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]: return -1
        if thres <= score[1]:
            if wanho_sum < sum(score): answer += 1
            thres = score[1]

    return answer