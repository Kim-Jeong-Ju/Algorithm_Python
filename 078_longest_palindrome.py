## 문제 078. 가장 긴 팰린드롬 --- 프로그래머스 Lv.3 연습 문제

def solution(string):
    answer, size = 0, len(string)

    for a in range(size):
        for b in range(a + 1, size + 1):
            now_check = string[a:b]
            if now_check == now_check[::-1]:
                if answer < b - a:
                    answer = b - a

    return answer