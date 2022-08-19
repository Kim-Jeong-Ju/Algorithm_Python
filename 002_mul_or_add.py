## 문제 002. 곱하기 혹은 더하기

# 각 자리가 숫자로만(0~9) 이루어진 문자열 S(1 <= S <= 20)에 대해 +와 X연산만을 이용하여 생성 가능한
# 최대값(20억 이하)을 만드는 프로그램을 작성하라. 모든 연산은 왼쪽에서부터 순서대로 이루어진다.

# Input : 첫째 줄에 여러 개의 숫자로 이루어진 문자열 S
# Output : 연산 가능한 최대 결과값

num_string = input()
result = int(num_string[0])

for idx in range(1, len(num_string)):
    now = int(num_string[idx])

    if (now == 0 or now == 1) or (result == 0 or result == 1):  # 0 혹은 1의 값이면 더하기
        result += now
    else:       # 그 이외의 값이면 곱하기
        result *= now

print(result)