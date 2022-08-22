## 문제 008. 아이스크림 얼려 먹기

# N X M 크기의 얼음 틀에 대해 구멍이 뚫린 부분은 0으로, 구멍이 막힌 부분은 1의 값으로 구성되어 있다. 구멍이 뚫려 있는
# 부분끼리 상하좌우로 연결되어 있다고 할 때, 생성 가능한 아이스크림의 총 경우의 수를 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 얼음 틀의 세로(N)와 가로(M) 입력 (1 <= N, M <= 1,000)
#         둘째 줄부터 N+1번째 줄까지 얼음 틀의 형태 입력
# Output : 생성 가능한 아이스크림의 총 갯수 출력

n, m = map(int, input().split())
graph = []
for _ in range(n):      # 얼음 틀 입력
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False


result = 0
for a in range(n):
    for b in range(m):
        if dfs(a, b) == True:
            result += 1

print(result)