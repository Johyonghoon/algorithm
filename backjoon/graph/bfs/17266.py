# 17266번 어두운 굴다리
# https://www.acmicpc.net/problem/17266

"""
점의 좌표가 채워지는 것으로 문제를 생각한다면 틀린다.

반례
10
2
0 9

이럴 경우 4와 5 사이의 면적은 채워지지 않기 때문
면적을 기준으로 문제를 풀이한다면 풀 수 있지 않을까?
"""

from collections import deque

# 1차원 BFS
N = int(input())
M = int(input())
lights = list(map(int, input().split()))

q = deque()
load = [-1 for _ in range(N)]
for light in lights:
    if light < N:
        load[light] = 1
        q.append(light)
    if 0 <= light - 1:
        load[light-1] = 1
        q.append(light-1)

while q:
    # print(q)
    # print(load)
    nx = q.popleft()
    for dx in [-1, 1]:
        ex = nx + dx
        if 0 <= ex < N:
            if load[ex] == -1:
                load[ex] = load[nx] + 1
                q.append(ex)

print(max(load))

"""
반례
10
2
0 9

4~5 사이가 비추어지지 않는다

비추어지는 면적을 기준으로 -1과 자기 자신 0을 하면 되지 않을까
"""