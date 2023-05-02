## 문제 071. N으로 표현 --- 프로그래머스 Lv.3 연습 문제

def solution(N, number):
    answer = 0

    if number == 1:
        answer = 2

    else:
        total_list = []
        for count in range(1, 9):
            part_set = set()
            part_set.add(int(str(N) * count))
            for idx in range(count - 1):
                for a_num in total_list[idx]:
                    for b_num in total_list[-idx - 1]:
                        part_set.add(a_num + b_num)
                        part_set.add(a_num - b_num)
                        part_set.add(a_num * b_num)
                        if b_num != 0: part_set.add(a_num // b_num)

            if number in part_set:
                answer = count
                break

            total_list.append(part_set)

        if answer == 0: answer = -1

    return answer