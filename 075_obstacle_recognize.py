## 문제 075. 장애물 인식 프로그램 --- Softeer Lv.2 연습 문제

import sys

def any_remain(array, size):
    for x in range(size):
        for y in range(size):
            if array[x][y] == "1":
                return True, [x, y]

    return False, None


def dfs(graph, size, start, count):
    a, b = start
    graph[a][b] = "0"  # visited = True 처리
    count += 1

    a_dir = [-1, 0, 0, 1]  # Up, Left, Right, Down 순서
    b_dir = [0, -1, 1, 0]

    for da, db in zip(a_dir, b_dir):
        if 0 <= a + da < size and 0 <= b + db < size and graph[a + da][b + db] == "1":
            count = dfs(graph, size, [a + da, b + db], count)

    return count


graph = []
size = int(input())
for _ in range(size):
    graph.append(list(sys.stdin.readline().rstrip()))

blocks = []
while any_remain(graph, size)[0] == True:
    start = any_remain(graph, size)[1]
    blocks.append(dfs(graph, size, start, 0))
blocks.sort()

print(len(blocks))
for block in blocks:
    print(block)