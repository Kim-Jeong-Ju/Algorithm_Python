## 문제 007. 문자의 재정렬

# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어졌을 때, 모든 알파벳을 오름차순으로 정렬하여 먼저 출력 후
# 모든 숫자를 더한 값을 이어서 출력하는 프로그램을 작성하라.

# Input : 첫째 줄에 하나의 문자열 S
# Output : 문제에서 요구하는 정답 출력

string = input()
alphas = ''
nums = []

for data in string:
    if data.isalpha():
        alphas += data
    else:
        nums.append(int(data))

arrange = ''.join(sorted(alphas))
summation = sum(nums)

print(arrange, end="")
print(summation)