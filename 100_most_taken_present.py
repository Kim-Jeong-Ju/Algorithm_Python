## 문제 099. 가장 많이 받은 선물 --- 프로그래머스 Lv.1 연습 문제

from itertools import combinations

def solution(friends, gifts):
    answer = 0
    array = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    present_dict1 = {key: 0 for key in friends}
    present_dict2 = {key: 0 for key in friends}

    for gift in gifts:
        A, B = gift.split()
        A_idx, B_idx = friends.index(A), friends.index(B)

        array[A_idx][B_idx] += 1
        present_dict1[A] += 1
        present_dict1[B] -= 1

    for AA, BB in combinations(friends, 2):
        AA_idx, BB_idx = friends.index(AA), friends.index(BB)

        if (array[AA_idx][BB_idx] != 0 or array[BB_idx][AA_idx] != 0) and (
                array[AA_idx][BB_idx] != array[BB_idx][AA_idx]):
            if array[AA_idx][BB_idx] > array[BB_idx][AA_idx]:
                present_dict2[AA] += 1
            else:
                present_dict2[BB] += 1
        else:
            if present_dict1[AA] > present_dict1[BB]:
                present_dict2[AA] += 1
            elif present_dict1[AA] < present_dict1[BB]:
                present_dict2[BB] += 1
            else:
                pass

    answer = max(present_dict2.values())
    return answer