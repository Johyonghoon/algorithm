# 1931번 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, end, cnt):
    global result
    # print(node, end, cnt)
    if node == N-1:
        result = max(result, cnt)
        return

    if cnt + (N - 1) - node < result:
        return

    for nxt in range(node+1, N):
        s, e = timelines[nxt]
        if s >= end:
            recur(nxt, e, cnt+1)


N = int(input())
timelines = []
extra = 0
for _ in range(N):
    start, end = list(map(int, input().split()))
    if start == end:
        extra += 1
    else:
        timelines.append([start, end])

N -= extra
# 타임라인으로 정렬하여 같은 시작시간을 가질 때, 더 짧은 시간의 회의인 경우만 남김
timelines.sort()
prv = -1
idx = 0
while idx < N:
    start, end = timelines[idx]
    if start == prv:
        timelines.pop(idx)
        N -= 1
        continue
    else:
        prv = start
        idx += 1

result = 0
recur(-1, 0, 0)
# 무조건 넣을 수 있는 회의시간의 개수를 추가
print(result + extra)


