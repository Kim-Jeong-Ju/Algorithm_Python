## 문제 025. 괄호 변환 --- 프로그래머스 Lv.2 연습 문제

def bracket_split(string):  # u와 v 2가지 string으로 나누는 작업
    left, right, stop = 0, 0, 0
    for idx, alpha in enumerate(string):
        if alpha == "(":
            left += 1
        else:
            right += 1

        if left == right:
            stop = idx
            break

    u = string[:stop + 1]
    v = string[stop + 1:]
    return u, v


def check_right(string):  # 올바른 괄호 문자열인지 판단하는 작업
    stack = []
    for alpha in string:
        if not stack:
            stack.append(alpha)
        else:
            if stack[-1] == "(":
                if alpha == ")":
                    stack.pop()
                else:
                    stack.append(alpha)
            else:
                return False

    if stack:
        return False
    else:
        return True


def wrong_case(string):
    string = string[1:-1]
    new_string = ""
    if not string:
        return new_string
    else:
        for alpha in string:
            if alpha == "(":
                new_string += ")"
            else:
                new_string += "("
        return new_string


def recursive_call(bracket):
    if bracket == "":
        return bracket
    else:
        u, v = bracket_split(bracket)
        if check_right(u):
            return u + recursive_call(v)
        else:
            next_u = wrong_case(u)
            return "(" + recursive_call(v) + ")" + next_u


def solution(bracket):
    answer = recursive_call(bracket)
    return answer