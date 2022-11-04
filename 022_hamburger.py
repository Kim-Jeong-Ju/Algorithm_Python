## 문제 021. 햄버거 만들기 - 프로그래머스 Lv.1 연습 문제

ingredient = "".join(list(map(int, input().split())))

answer = 0
stack = []

for ing in ingredient:
    stack.append(ing)

    if len(stack) >= 4:
        bread1, veg, meat, bread2 = stack[-4], stack[-3], stack[-2], stack[-1]
        if bread1 == 1 and veg == 2 and meat == 3 and bread2 == 1:
            del stack[-4:]
            answer += 1

print(answer)