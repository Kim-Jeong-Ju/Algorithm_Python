## 문제 086. 어른 상어 --- 백준 No.19237 연습 문제

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

array = []      # 상어가 현재 위치하는 전체 array 및 smell 현황 matrix
for _ in range(N):
    array.append(list(map(int, input().split())))

starts = []                                                 # 상어의 첫 위치 좌표 list
for a in range(N):
    for b in range(N):
        if array[a][b] != 0:
            starts.append([array[a][b], a, b, True])        # starts = [상어 번호, Row좌표, Col좌표, 생사 여부]
            array[a][b] = [array[a][b], K]                  # 상어O 위치의 smells = [상어 번호, 남은 Count]
        else:
            array[a][b] = [0, 0]                            # 상어X 위치의 smells = [0, 0]

before_dir = [0]
before_dir.extend(list(map(int, input().split())))          # 각 상어들의 첫(이전) 방향 list

move_crit = [[]]                    # move_crit[M번 상어][현재 방향] = 현재 방향에 대한 우선 순위 list
for _ in range(M):                  # M번 각각의 상어에 대하여
    now_shark = {}
    for direct in range(1, 5):      # 1(Up), 2(Down), 3(Left), 4(Right)에 대하여
        now_shark[direct] = list(map(int, input().split()))
    move_crit.append(now_shark)

da = [0, -1, 1, 0, 0]               # 0(Non-Usage), 1(Up), 2(Down), 3(Left), 4(Right) 순서
db = [0, 0, 0, -1, 1]


def calc_smell(array, shark):
    for a in range(N):
        for b in range(N):
            if array[a][b][0] == shark:
                array[a][b][1] -= 1             # before 좌표에서 Count --
                if array[a][b][1] == 0:         # Count 모두 소모했으면 0으로 재초기화
                    array[a][b] = [0, 0]

    return array


def end_point(shark_infos):
    is_end = True
    for shark_info in shark_infos:
        if shark_info[0] != 1 and shark_info[3] == True:
            is_end = False
            break

    return is_end


def bfs(array, move_crit, starts, before_dir, N, K):
    time = 0
    shark_infos = sorted(starts, key=lambda x: x[0])

    while time <= 1000:
        if end_point(shark_infos):      # 1번 상어를 제외하고 모두 죽었다면
            break

        for idx1, shark_info in enumerate(shark_infos):
            shark, a, b, check = shark_info    # 상어 번호, Row좌표, Col좌표, 생사 여부(T/F)

            if check:       # 살아있으면

                # Boundary 조건 내에 움직일 수 있는 좌표들 list 생성
                avail_moves = [[a+da[seq], b+db[seq]] for seq in range(1, 5) if 0 <= a+da[seq] < N and 0 <= b+db[seq] < N]
                empty_coords = []       # 아무도 지나오지 않은 길
                past_coords = []        # 내가 지나왔던 길
                for Atemp, Btemp in avail_moves:
                    if array[Atemp][Btemp] == [0, 0]: empty_coords.append([Atemp, Btemp])
                    elif array[Atemp][Btemp][0] == shark: past_coords.append([Atemp, Btemp])

                if len(empty_coords) != 0:                                          # 아무도 지나오지 않은 길 중에
                    for after_dir in move_crit[shark][before_dir[shark]]:           # 우선 순위 순서대로 확인하며
                        aa, bb = a+da[after_dir], b+db[after_dir]
                        if [aa, bb] in empty_coords:                                # 갈 수 있으면 update
                            shark_infos[idx1] = [shark, aa, bb, True]
                            before_dir[shark] = after_dir
                            break
                elif len(past_coords) != 0:                                         # 내가 지나왔던 길 중에
                    for after_dir in move_crit[shark][before_dir[shark]]:           # 우선 순위 순서대로 확인하며
                        aa, bb = a + da[after_dir], b + db[after_dir]
                        if [aa, bb] in past_coords:                                 # 갈 수 있으면 update
                            shark_infos[idx1] = [shark, aa, bb, True]
                            before_dir[shark] = after_dir
                            break

            else:           # 죽어있으면
                pass

        already_used = []
        for idx2, shark_info in enumerate(shark_infos):     # 움직여야 하는 후보군을 상어 번호 기준 오름차순으로 확인하며
            shark, aa, bb, check = shark_info
            array = calc_smell(array, shark)                # 최종 도착지를 제외한 지나왔던 길에 대해 냄새 -1 처리 이후

            if check:                                           # 살아있는 상어들에 대해서만
                if (aa, bb) not in already_used:                # 상어 번호가 큰 순으로 도착지를 선점하여
                    already_used.append((aa, bb))
                    array[aa][bb] = [shark, K]                  # 해당 after Row좌표, Col좌표에 대해 update
                else:
                    shark_infos[idx2][3] = False                # 큰 번호에 의해 밀려 작은 번호의 상어는 dead 처리

        time += 1

    if time > 1000:
        time = -1

    return time

answer = bfs(array, move_crit, starts, before_dir, N, K)
print(answer)