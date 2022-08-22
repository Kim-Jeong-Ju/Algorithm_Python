## Coefficient Sorting Algorithm Example Code

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)      # 주어진 list의 maximum을 최대 index로 하는 count list 생성

for idx in range(len(array)):       # 주어진 list의 모든 원소들에 대해
    count[array[idx]] += 1          # 몇 번 출현하는지 확인하여 count list에 입력

for a in range(len(count)):         # count list의 길이 만큼
    for b in range(count[a]):       # count list의 index값이 얼마나 출현하는지 만큼
        print(a, end=" ")           # index값을 출력