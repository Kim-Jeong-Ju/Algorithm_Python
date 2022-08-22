## 문제 011. 떡볶이 떡 만들기

# 줄지어진 떡을 높이 H를 지정하면 한번에 H만큼 자른다고 하자. H보다 길이가 긴 떡은 H로 잘릴 것이고, H보다 길이가 작은 떡은 그대로일 것이다.
# 적어도 잘리게 된 길이 M만큼 손님이 가져간다고 하자. 손님이 요청한 떡의 길이 M에 대해 설정 가능한 절단기의 높이 H의 최댓값을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 요청한 떡의 갯수 N과 떡의 길이 M 입력 (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
#         둘째 줄에 떡의 개별 높이
# Output : 손님이 적어도 M만큼의 떡을 가져가기 위해 설정 가능한 절단기의 높이 H의 최댓값 출력

n, m = map(int, input().split())
cakes = list(map(int, input().split()))

cakes.sort()

start = 0               # start index = 0
end = max(cakes)        # end index = 떡 배열에서의 최대 길이


result_height = 0

while start <= end:
    get_cakes = 0                      # 자른 후 손님이 가져가게 될 떡의 양
    height = (start + end) // 2        # 중간점 설정

    for cake in cakes:
        if cake > height:
            get_cakes += cake - height

    if get_cakes >= m:
        result_height = height
        start = height + 1
    else:
        end = height - 1

print(result_height)