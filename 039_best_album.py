## 문제 039. 베스트 앨범 --- 프로그래머스 Lv.3 연습 문제

def solution(genres, plays):
    answer = []
    music, total = {}, 0
    for a, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in music.keys():
            music[genre] = [[a, play, play]]
        else:
            music[genre].append([a, play, music[genre][-1][2] + play])

    music = dict(sorted(music.items(), reverse=True, key=lambda x: x[1][-1][2]))
    for key, value in music.items():
        music[key] = sorted(music[key], reverse=True, key=lambda x: (x[1], -x[0]))

    for times in music.values():
        if len(times) == 1:
            answer.append(times[0][0])
        else:
            answer.extend([times[0][0], times[1][0]])

    return answer