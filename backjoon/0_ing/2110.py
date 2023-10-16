# 2110번 공유기 설치
# https://www.acmicpc.net/problem/2110

"""
# 이분탐색
집 N개의 좌표가 주어진다.
한 집에 하나의 공유기만 설치할 수 있고, C개 설치한다.
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
"""

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort(reverse=True)
print(house)

dist = []
for j in range(N-1):
    dist.append(house[j]-house[j+1])
dist.sort(reverse=True)
print(dist)

start = house[-1] + 1
end = house[0] - 1
result = end

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for idx in range(N-1):
        cnt += (dist[idx]-1) // mid
    if cnt >= C:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1
print(result)




