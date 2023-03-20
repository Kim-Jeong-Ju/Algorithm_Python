## 문제 048. 디스크 컨트롤러 --- 프로그래머스 Lv.3 연습 문제

import heapq

def solution(jobs):
    answer = 0

    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))         # 모든 작업에 대해 시작 시간, 소요 시간 순으로 오름차순 정렬
    heap = []
    before, after, fin_count = -1, 0, 0                     # before = 시작 시간 lower bound, after = 시작 시간 upper bound

    while fin_count < len(jobs):                            # fin_count = 종료된 작업의 갯수
        for start, work in jobs:
            if before < start <= after:
                heapq.heappush(heap, (work, start))         # heap에는 우순순위를 고려해 (소요 시간, 시작 시간) 으로 삽입

        if heap:                                            # 현재 시간에 처리할 수 있는 작업 O
            cur_work, cur_start = heapq.heappop(heap)
            before = after                                  # 시작 시간 탐색에 대한 range를 현재 작업을 기준으로 변경
            after += cur_work
            answer += after - cur_start                     # (종료 시간 - 요청 시간) 누적합 계산
            fin_count += 1                                  # 종료된 작업의 갯수 + 1
        else:                                               # 현재 시간에 처리할 수 있는 작업 O
            after += 1                                      # 시작 시간 upper bound만 넓혀서 재탐색

    answer = int(answer / len(jobs))
    return answer