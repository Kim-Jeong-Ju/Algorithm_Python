## 문제 099. 가장 많이 받은 선물 --- 프로그래머스 Lv.1 연습 문제

from itertools import product

def solution(users, emoticons):
    answer = []
    size = len(emoticons)
    rates, result = [10, 20, 30, 40], []

    disc_cases = list(product(rates, repeat=size))
    for disc_case in disc_cases:
        people, total_price = 0, 0
        for user_rate, user_price in users:
            buy_price = 0
            for idx in range(size):
                if user_rate <= disc_case[idx]:
                    buy_price += emoticons[idx] - (emoticons[idx] * disc_case[idx] * 0.01)

            if buy_price >= user_price: people += 1
            else: total_price += buy_price

        result.append([people, int(total_price)])

    answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))[0]
    return answer