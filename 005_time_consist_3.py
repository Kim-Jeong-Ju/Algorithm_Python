## 문제 005. 숫자 3을 포함하는 시각 세기

# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되어 있는 모든 경우의 수를
# 세는 프로그램을 작성하라.

# Input : 첫째 줄에 입력될 시각 정수 N(1 <= N <= 23)
# Output : 3이 하나라도 포함되는 모든 시각의 경우의 수

n = int(input())

result = 0

for hour in range(n + 1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(min) + str(sec):
                result += 1

print(result)