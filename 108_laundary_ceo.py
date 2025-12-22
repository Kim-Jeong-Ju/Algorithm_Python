"""
    # ! 문제 108. 세탁소 사장 동혁 --- 백준 No.2720
"""

T = int(input())

for _ in range(T):
    Array = [25, 10, 5, 1]
    Brray = [0, 0, 0, 0]

    amount = int(input())

    for idx in range(4):
        div, mod = divmod(amount, Array[idx])

        amount -= Array[idx] * int(div)
        Brray[idx] += int(div)

    print(f"{Brray[0]} {Brray[1]} {Brray[2]} {Brray[3]}")