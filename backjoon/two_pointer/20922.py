# 20922번 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922

"""
수열을 순서대로 탐색하며 K개 초과 포함되지 않는다면 카운트
K개를 초과한다면, 그 숫자가 처음 나온 인덱스 다음 인덱스부터 시작

투포인터
"""
from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

d = {}
cnt = 0
result = 0
idx = 0
while idx < N:
    if arr[idx] not in d:
        d[arr[idx]] = deque()
        d[arr[idx]].append(idx)
        cnt += 1
    else:
        d[arr[idx]].append(idx)
        if len(d[arr[idx]]) > K:
            cnt = 0
            idx = d[arr[idx]].popleft() + 1
            d = {}
            continue
        else:
            cnt += 1

    result = max(result, cnt)
    idx += 1

print(result)

"""
10 2
1 2 3 3 3 4 5 6 7 8

10 2
1 2 3 2 3 3 4 5 6 7
"""