## 문제 080. 호텔 대실 --- 프로그래머스 Lv.2 연습 문제

def solution(book_times):
    answer = 0
    array = []
    for book_time in book_times:
        start = (int(book_time[0][:2]) * 60) + int(book_time[0][3:])
        end = (int(book_time[1][:2]) * 60) + int(book_time[1][3:])
        array.append([start, end + 10])
    array = sorted(array, key=lambda x: x[0])

    rooms = []
    for a, info in enumerate(array):
        if a == 0:
            rooms.append(info)
        else:
            new_start, new_end = info[0], info[1]
            append_idx = -1
            for b, room in enumerate(rooms):
                plus_room = False
                old_starts, old_ends = room[::2], room[1::2]
                for old_start, old_end in zip(old_starts, old_ends):
                    if new_end <= old_start or new_start >= old_end:
                        pass  # 방 유지
                    else:
                        plus_room = True  # 방 추가
                        break

                if not plus_room:
                    append_idx = b
                    break

            if append_idx != -1:
                rooms[append_idx].extend([new_start, new_end])
            else:
                rooms.append(info)

    answer = len(rooms)
    return answer