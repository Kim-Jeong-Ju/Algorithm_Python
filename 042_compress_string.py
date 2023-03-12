## 문제 042. 문자열 압축 --- 프로그래머스 Lv.2 연습 문제

def solution(string):
    answer = 0

    min_length = len(string)
    for a in range(1, len(string) // 2 + 1):
        word_info = []
        for b in range(0, len(string), a):
            if string[b:b + a] not in word_info:
                word_info.extend(["1", string[b:b + a]])
            else:
                if word_info[-1] == string[b:b + a]:
                    word_info[-2] = str(int(word_info[-2]) + 1)
                else:
                    word_info.extend(["1", string[b:b + a]])

        word_info = [value for value in word_info if value != "1"]
        new_string = "".join(word_info)

        if len(new_string) < min_length:
            min_length = len(new_string)

    answer = min_length
    return answer