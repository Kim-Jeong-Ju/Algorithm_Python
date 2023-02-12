## 문제 034. 혼자 놀기의 달인 --- 프로그래머스 Lv.2 연습 문제

def group_count(num, cards, visited):
    if num not in visited:
        visited.append(num)
        return group_count(cards[num-1], cards, visited)

    return visited, len(visited)

def solution(cards):
    answer = 0
    count_list = []
    visited = []

    for card in cards:
        if not count_list:
            visited, cnt = group_count(card, cards, visited)
            count_list.append(cnt)
        else:
            if card not in visited:
                visited, cnt = group_count(card, cards, visited)
                count_list.append(cnt - sum(count_list))
            else:
                pass

    if len(count_list) == 1:
        pass
    else:
        count_list = sorted(count_list, reverse=True)
        answer = count_list[0] * count_list[1]

    return answer