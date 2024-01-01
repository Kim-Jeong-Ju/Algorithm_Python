## 문제 099. 이모티콘 할인행사 --- 프로그래머스 Lv.2 연습 문제

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


users1 = [[40, 10000], [25, 10000]]
emoticons1 = [7000, 9000]
print(solution(users1, emoticons1))
print()

users2 = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons2 = [1300, 1500, 1600, 4900]
print(solution(users2, emoticons2))