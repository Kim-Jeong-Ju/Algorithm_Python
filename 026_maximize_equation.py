## 문제 026. 수식 최대화 - 프로그래머스 Lv.2 연습 문제

from itertools import permutations


def calc(num1, operand, num2):
    if operand == "+":
        return str(int(num1) + int(num2))
    elif operand == "-":
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))


def solution(expression):
    answer = 0

    equations = []
    opers = []
    num = ""
    for idx, alpha in enumerate(expression):
        if idx == len(expression) - 1:
            num += alpha
            equations.append(num)
        else:
            if alpha.isdigit():
                num += alpha
            else:
                equations.append(num)
                equations.append(alpha)
                num = ""
    for beta in expression:
        if (beta == "+" or beta == "-" or beta == "*") and beta not in opers:
            opers.append(beta)
    print(equations)

    cases = list(permutations(opers, len(opers)))
    print(cases)
    print()

    maxi = 0
    for case in cases:
        array = []
        for idx, operand in enumerate(case):
            pass_idx = -1

            if idx == 0:
                stack = []
                for a in range(len(equations)):
                    if a == pass_idx: continue
                    if equations[a] == operand:
                        last = stack.pop()
                        stack.append(calc(last, operand, equations[a + 1]))
                        pass_idx = a+1
                    else:
                        stack.append(equations[a])
                    print(stack)
                array.append(stack)

            else:
                last_equat = array[-1]
                stack = []
                for b in range(len(last_equat)):
                    if b == pass_idx: continue
                    if last_equat[b] == operand:
                        last = stack.pop()
                        stack.append(calc(last, operand, last_equat[b + 1]))
                        pass_idx = b + 1
                    else:
                        stack.append(last_equat[b])
                    print(stack)
                array.append(stack)

        now = abs(int(array[-1][0]))
        if now >= maxi: maxi = now

    answer = maxi
    return answer