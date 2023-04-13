## 문제 062. 불량 사용자 --- 프로그래머스 Lv.3 연습 문제

from itertools import permutations

def solution(user_ids, banned_ids):
    answer = []

    for permute in permutations(user_ids, len(banned_ids)):
        add_answer = False
        for banned_word, permute_word in zip(banned_ids, list(permute)):
            if len(banned_word) == len(permute_word):
                for alpha, beta in zip(banned_word, permute_word):
                    if alpha == "*":
                        add_answer = True
                    elif alpha != "*" and alpha == beta:
                        add_answer = True
                    else:
                        add_answer = False
                        break

                if not add_answer: break
            else:
                add_answer = False
                break

        if add_answer and set(permute) not in answer:
            answer.append(set(permute))

    return len(answer)