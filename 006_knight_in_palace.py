## 문제 006. 왕실의 나이트

# 8 X 8 체스판 형식의 왕실에 나이트가 있다. 나이트는 왕실 내에서 L자 형태로 움직일 수 있으며, 그 밖으로는 이동 불가하다.
# 수평으로 2칸 이동 후 수직으로 1칸 이동 or 수평으로 1칸 이동 후 수직으로 2칸 이동 가능하며, 행 위치는 1~8의 숫자로,
# 열 위치는 a~h의 문자로 표현할 때, 특정 위치에서 이동 가능한 경우의 수를 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 나이트가 위치한 좌표를 공백 없이 입력(열행 순으로)
# Output : 나이트가 이동 가능한 모든 경우의 수

cord = input()
cord_row = int(cord[1])
cord_col = ord(cord[0]) - 97 + 1

dx = [+1, -1, +2, -2, +2, -2, +1, -1]   # 체스판 내에서 나이트가 이동 가능한 모든 경우의 수
dy = [-2, -2, -1, -1, +1, +1, +2, +2]

before_x = cord_row
before_y = cord_col
result = 0

for ix, iy in zip(dx, dy):
    if before_x + ix >= 1 and before_x + ix <= 8 and before_y + iy >= 1 and before_y + iy <= 8:
        result += 1

print(result)