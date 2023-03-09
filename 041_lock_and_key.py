## 문제 041. 자물쇠와 열쇠 --- 프로그래머스 Lv.3 연습 문제

import copy

def open_check(a, b, key, array, key_size, lock_size):
    origin = copy.deepcopy(array)
    lock_sum = 0

    for row1 in range(key_size):
        for col1 in range(key_size):
            array[a + row1][b + col1] += key[row1][col1]

    for row2 in range(key_size, key_size + lock_size):
        for col2 in range(key_size, key_size + lock_size):
            if array[row2][col2] == 0 or array[row2][col2] == 2:
                return False, origin
    return True, origin


def spin_key(key):
    new_key = []
    for col in range(len(key)):
        spinned = []
        for row in range(len(key) - 1, -1, -1):
            spinned.append(key[row][col])
        new_key.append(spinned)

    return new_key


def solution(key, lock):
    answer = True

    key_size, lock_size = len(key), len(lock)
    new_size = lock_size + (2 * key_size)
    array = [[0 for _ in range(new_size)] for _ in range(new_size)]
    for a in range(new_size):
        for b in range(new_size):
            if key_size <= a < key_size + lock_size and key_size <= b < key_size + lock_size:
                array[a][b] = lock[a - key_size][b - key_size]

    for _ in range(4):
        for a in range(new_size - key_size + 1):
            for b in range(new_size - key_size + 1):
                is_open, array = open_check(a, b, key, array, key_size, lock_size)
                if is_open: return answer

        key = spin_key(key)

    answer = False
    return answer