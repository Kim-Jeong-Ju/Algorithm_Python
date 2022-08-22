## 문제 004. 상하좌우

# N X N 크기의 정사각형 공간에 대해 가장 왼쪽 위의 좌표(1, 1), 가장 오른쪽 아래 좌표(N, N)이며, 시작 좌표는 (1, 1)이다.
# L(왼쪽으로 한칸), R(오른쪽으로 한칸), U(위쪽으로 한칸), D(아래쪽으로 한칸)로 공간 내에서 이동할 수 있으며, 공간 밖을 벗어나는
# 움직임은 무시된다. 최종 도착 지점의 좌표를 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 공간의 크기 N(1 <= N <= 100), 둘째 줄에 여행가가 이동할 계획서 내용(1 <= 이동 횟수 <= 100)
# Output : 여행가의 최종 목적지 좌표

n = int(input())
moves = list(map(str, input().split()))

dx = [-1, +1, 0, 0]     # 왼쪽부터 차례대로 U, D, L, R 순서
dy = [0, 0, -1, +1]     # 왼쪽부터 차례대로 U, D, L, R 순서

final_x = 1     # 출발 좌표
final_y = 1

for move in moves:
    if move == "U":      # U가 입력된 경우
        if final_x + dx[0] >= 1:
            final_x += dx[0]
            final_y += dy[0]
    elif move == "D":    # D가 입력된 경우
        if final_x + dx[1] <= n:
            final_x += dx[1]
            final_y += dy[1]
    elif move == "L":    # L이 입력된 경우
        if final_y + dy[2] >= 1:
            final_x += dx[2]
            final_y += dy[2]
    elif move == "R":    # R이 입력된 경우
        if final_y + dy[3] <= n:
            final_x += dx[3]
            final_y += dy[3]

print(final_x, final_y)