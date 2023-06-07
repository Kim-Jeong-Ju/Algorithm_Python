## 문제 084. 풍선 터뜨리기 --- 프로그래머스 Lv.3 연습 문제

def solution(array):
    answer = 0

    left, right = [], []
    left_min, right_min = array[0], array[-1]

    for alpha in array:
        if alpha < left_min: left_min = alpha
        left.append(left_min)

    for beta in array[::-1]:
        if beta < right_min: right_min = beta
        right.append(right_min)

    answer = len(set(left + right))
    return answer