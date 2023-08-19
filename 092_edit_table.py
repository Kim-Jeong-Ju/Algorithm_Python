## 문제 092. 표 편집 --- 프로그래머스 Lv.3 연습 문제

def solution(n, k, commands):
    answer = ['O'] * n

    info = {num: [num-1, num+1] for num in range(n)}
    info[0] = [None, 1]
    info[n-1] = [n-2, None]

    deleted, idx = [], k
    for command in commands:
        if command[0] == 'U' or command[0] == 'D':
            state, size = command.split(' ')
            if state == 'U':
                for _ in range(int(size)): idx = info[idx][0]
            else:
                for _ in range(int(size)): idx = info[idx][1]

        elif command == 'C':
            answer[idx] = 'X'
            before, after = info[idx]
            deleted.append([before, idx, after])

            ## 커서 이동 처리
            if after == None:           # array의 가장 마지막 원소이면, 이전으로 커서 이동
                idx = info[idx][0]
            else:                       # array의 일반적인 원소이면, 다음으로 커서 이동
                idx = info[idx][1]

            ## 삭제하려는 원소의 인접한 전후 원소의 연결 여부 처리
            if before == None:          # 삭제하려는 원소 = 첫번째 원소이면
                info[after][0] = None
            elif after == None:         # 삭제하려는 원소 = 마지막 원소이면
                info[before][1] = None
            else:                       # 삭제하려는 원소 = 일반적인 원소이면
                info[before][1] = after
                info[after][0] = before

        else:
            prev, now, next = deleted.pop()
            answer[now] = 'O'
            if prev == None:
                info[next][0] = now
            elif next == None:
                info[prev][1] = now
            else:
                info[prev][1] = now
                info[next][0] = now

    answer = "".join(answer)
    return answer


n1, k1, commands1 = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n1, k1, commands1))
print()

n2, k2, commands2 = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n1, k1, commands2))