# 3079번 입국심사
# https://www.acmicpc.net/problem/3079

"""
이분탐색 - 파라메트릭 서치
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
immigrations = []
for _ in range(N):
    immigrations.append(int(input()))
immigrations.sort(reverse=True)

start = 0
end = immigrations[0] * M
result = end
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for idx in range(N):
        cnt += mid // immigrations[idx]
    if cnt >= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
    # print(mid, cnt)

print(result)


