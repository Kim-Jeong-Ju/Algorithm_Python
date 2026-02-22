"""
    # ! 문제 112. 잃어버린 괄호 --- 백준 No.1541
"""

Array = list(map(str, input().split('-')))
for idx1, alpha in enumerate(Array):
    if '+' in alpha:  Array[idx1] = sum(list(map(int, alpha.split('+'))))
    else:             Array[idx1] = int(alpha)

answer = Array[0]
for idx2 in range(1, len(Array)):
    answer -= Array[idx2]

print(answer)