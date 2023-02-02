## 문제 031. 거리두기 확인하기 --- 프로그래머스 Lv.2 연습 문제

from itertools import combinations


def solution(places):
    answer = []

    for place in places:
        array = []
        for line in place:
            array.append(list(line))

        people = []
        for a in range(5):
            for b in range(5):
                if array[a][b] == "P": people.append([a, b])

        is_okay = True
        for idx, combine in enumerate(combinations(people, 2)):
            print(idx + 1, combine)
            a_person, b_person = combine[0], combine[1]
            ax, ay, bx, by = a_person[0], a_person[1], b_person[0], b_person[1]

            if abs(ax - bx) + abs(ay - by) > 2:
                pass

            elif abs(ax - bx) + abs(ay - by) == 2:
                if ax == bx:  # 수평 관계
                    if array[ax][min(ay, by) + 1] != "X":
                        is_okay = False
                        break
                elif ay == by:  # 수직 관계
                    if array[min(ax, bx) + 1][ay] != "X":
                        is_okay = False
                        break
                else:  # 대각선 관계
                    if (array[max(ax, bx)][min(ay, by)] != "X" or array[min(ax, bx)][max(ay, by)] != "X") and (
                            array[max(ax, bx)][max(ay, by)] != "X" or array[min(ax, bx)][min(ay, by)] != "X"):
                        is_okay = False
                        break

            else:
                is_okay = False
                break

        if is_okay:
            answer.append(1)
        else:
            answer.append(0)

    return answer