## 문제 102. Addition Cycle --- 백준 No.1110

cycle = 0

old_num = input()
new_num = '-1'

while int(old_num) != int(new_num):
    if new_num == '-1':
        if len(old_num) == 1:
            new_num = old_num + old_num
        else:
            if len(str(int(old_num[0]) + int(old_num[1]))) == 1:
                new_num = old_num[1] + str(int(old_num[0]) + int(old_num[1]))[0]
            else:
                new_num = old_num[1] + str(int(old_num[0]) + int(old_num[1]))[1]
    else:
        if len(str(int(new_num[0]) + int(new_num[1]))) == 1:
            new_num = new_num[1] + str(int(new_num[0]) + int(new_num[1]))[0]
        else:
            new_num = new_num[1] + str(int(new_num[0]) + int(new_num[1]))[1]

    cycle += 1

print(cycle)