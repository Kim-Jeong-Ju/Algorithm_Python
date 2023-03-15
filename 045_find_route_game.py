## 문제 045. 길 찾기 게임 --- 프로그래머스 Lv.3 연습 문제

import sys
sys.setrecursionlimit(10 ** 9)

def pre_order(arrX, arrY, result):
    root = arrY[0]
    idx = arrX.index(root)
    left_childs, right_childs = [], []

    for a in range(1, len(arrY)):
        if root[1] > arrY[a][1]: left_childs.append(arrY[a])
        else: right_childs.append(arrY[a])

    result.append(root[0])
    if left_childs: pre_order(arrX[:idx], left_childs, result)
    if right_childs: pre_order(arrX[idx+1:], right_childs, result)

    return result


def post_order(arrX, arrY, result):
    root = arrY[0]
    idx = arrX.index(root)
    left_childs, right_childs = [], []

    for b in range(1, len(arrY)):
        if root[1] > arrY[b][1]:
            left_childs.append(arrY[b])
        else:
            right_childs.append(arrY[b])

    if left_childs: post_order(arrX[:idx], left_childs, result)
    if right_childs: post_order(arrX[idx + 1:], right_childs, result)
    result.append(root[0])

    return result


def solution(nodeinfo):
    answer = []
    pre_result, post_result = [], []

    nodeinfo = [[idx+1, a, b] for idx, (a, b) in enumerate(nodeinfo)]
    arrX = sorted(nodeinfo, key=lambda x: x[1])
    arrY = sorted(nodeinfo, reverse=True, key=lambda x: (x[2], -x[1]))

    pre_result = pre_order(arrX, arrY, [])
    post_result = post_order(arrX, arrY, [])

    answer = [pre_result, post_result]
    return answer