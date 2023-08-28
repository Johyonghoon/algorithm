# 1244번 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline


def onoff(x):
    if x:
        return 0
    else:
        return 1


N = int(input())
switch = [0] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:  # 남학생 == 1
        idx = 1
        while idx * num <= N:
            switch[idx*num] = onoff(switch[idx*num])
            idx += 1
    else:            # 여학생 == 2
        switch[num] = onoff(switch[num])
        idx = 1
        while num - idx > 0 and num + idx <= N:
            if switch[num-idx] == switch[num+idx]:
                switch[num-idx] = onoff(switch[num-idx])
                switch[num+idx] = onoff(switch[num+idx])
                idx += 1
            else:
                break

switch.pop(0)
while len(switch) > 20:
    print(*switch[:20])
    switch = switch[20:]
print(*switch)
