"""
    # ! 문제 111. 서버 증설 횟수 --- 프로그래머스 Lv.2 연습 문제
"""

def solution(players, m, k):
    answer = 0
    add_server = [0 for _ in range(24)]
    
    for idx, player in enumerate(players):
        if idx-k >= 0 and add_server[idx-k] >= 1:
            add_server[idx-k] = 0
        
        if (player // m >= 1 and (player // m) > sum(add_server)):
            add_server[idx] = player // m - sum(add_server)
            answer += add_server[idx]
    
    return answer