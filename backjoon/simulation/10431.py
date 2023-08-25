# 10431번 줄세우기
# https://www.acmicpc.net/problem/10431

import sys
input = sys.stdin.readline

"""
문제 해석을 잘못했다.
정렬된 곳에 한 명이라도 키 큰 사람이 있다면, 맨 앞으로 보내고 재정렬을 하는 줄 알았지만,
알고보니 맨 뒤에 서고서 앞과 비교하며 클 경우에만 변경하고 카운트하는 것이었다.
문제 해석이 제일 어렵다. (그래서 왜 이게 실버5 인거지 생각함...) 
"""


P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    tc = arr[0]
    students = arr[1:]

    cnt = 0
    line = []
    maxi = 0
    for student in students:
        # print(maxi, cnt, line)
        line += [student]
        if maxi < student:
            maxi = student
        else:
            for idx in range(len(line)-1, 0, -1):
                if line[idx-1] > line[idx]:
                    cnt += 1
                    line[idx-1], line[idx] = line[idx], line[idx-1]
                else:
                    break

    print(tc, cnt)



