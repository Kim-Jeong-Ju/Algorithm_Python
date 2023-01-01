## 문제 023. 뉴스 클러스터링 --- 프로그래머스 Lv.2 연습 문제

from collections import Counter

answer = 0
str1 = input()
str2 = input()

str1, str2 = str1.lower(), str2.lower()
string1 = []
string2 = []

for a in range(len(str1) - 1):
    alphas = str1[a:a + 2]
    if alphas.isalpha():
        string1.append(alphas)
for b in range(len(str2) - 1):
    betas = str2[b:b + 2]
    if betas.isalpha():
        string2.append(betas)

counter1, counter2 = Counter(string1), Counter(string2)

if len(counter1) == 0 and len(counter2) == 0:
    answer = 1
else:
    inter = len(list((counter1 & counter2).elements()))
    union = len(list((counter1 | counter2).elements()))
    answer = inter / union
print(answer)