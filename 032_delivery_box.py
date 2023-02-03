## 문제 032. 택배 상자 --- 프로그래머스 Lv.2 연습 문제

def solution(order):
    answer = 0

    size = len(order)
    stack = []
    box = 1

    while box != size + 1:
        stack.append(box)
        while stack[-1] == order[answer]:
            answer += 1
            stack.pop()

            if len(stack) == 0:
                break
        box += 1

    return answer