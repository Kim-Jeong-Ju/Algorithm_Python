## 문제 055. 단어 변환 --- 프로그래머스 Lv.3 연습 문제

from collections import defaultdict


def diff_count(word1, word2):
    count = 0
    for alpha, beta in zip(word1, word2):
        if alpha != beta: count += 1

    if count == 1:
        return True
    else:
        return False


def dfs(graph_dict, visited, begin, target, array):
    visited[begin] = True
    array.append(begin)

    if begin == target:
        return array

    for adjacent in graph_dict[begin]:
        if visited[adjacent] == False:
            array = dfs(graph_dict, visited, adjacent, target, array)
            if array[-1] != target:
                visited[adjacent] = False
                array.pop()
            else:
                break

    return array


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    graph_dict = defaultdict(list)
    graph_dict[begin] = []
    graph_dict[target] = []

    for word in words:
        if word not in graph_dict.keys(): graph_dict[word] = []

    graph_keys = list(graph_dict.keys())
    for a, key1 in enumerate(graph_keys):
        for b, key2 in enumerate(graph_keys):
            if a != b and diff_count(key1, key2): graph_dict[key1].append(key2)

    visited = {graph_key: False for graph_key in graph_keys}
    array = dfs(graph_dict, visited, begin, target, [])

    answer = len(array) - 1
    return answer