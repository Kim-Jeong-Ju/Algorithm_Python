"""
    # ! 문제 114. 약수들의 합 --- 백준 No.9506
"""

import math


def array_of_divisor(value):
    array = [1]

    for num in range(2, int(math.sqrt(value))+1):
        if value % num == 0:
            array.extend([num, value // num])
    
    array.sort()

    if sum(array) == value: return array
    else:                   return None

while True:
    alpha = int(input())
    answer = str(alpha)

    if alpha != -1:
        Array = array_of_divisor(alpha)

        if Array != None:
            answer += ' = '

            for idx in range(len(Array)):
                if idx != len(Array) - 1: answer += str(Array[idx]) + ' + '
                else:                     answer += str(Array[idx])
        else:
            answer += ' is NOT perfect.'
        
        print(answer)
    else:
        break