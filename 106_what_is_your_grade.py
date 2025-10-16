## 문제 106. 너의 평점은 --- 백준 No.25206

A_tot_grade, B_tot_grade = 0, 0

alpha_crit = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
              'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for _ in range(20):
    Array = list(input().split())

    subject, A_grade, B_grade = Array[0], float(Array[1]), Array[2]

    if B_grade != 'P':
        A_tot_grade += A_grade * alpha_crit[B_grade]
        B_tot_grade += A_grade

print('%.6f' % (A_tot_grade / B_tot_grade))
