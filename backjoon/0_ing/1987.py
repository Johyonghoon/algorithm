# 1987번 알파벳
# https://www.acmicpc.net/problem/1987

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

R, C = map(int, input().split())
# 보드 정보
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

q = deque()
q.append([0, 0, set(graph[0][0])])

result = 0

while q:
    ny, nx, nset = q.popleft()
    result = max(result, len(nset))
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = ny + dy
        ex = nx + dx

        if 0 <= ey < R and 0 <= ex < C:
            if graph[ey][ex] in nset:
                continue
            eset = list(nset)
            eset.append(graph[ey][ex])
            eset = set(eset)
            q.append([ey, ex, eset])


print(result)




"""
# dfs + set :: 시간 초과

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(ny, nx, seti):
    global result

    result = max(result, len(seti))
    # 방문처리를 할 필요가 없는 이유?
    # 자기 자신과 같은 알파벳은 탐색할 수 없기 때문
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = ny + dy
        ex = nx + dx

        if 0 <= ey < R and 0 <= ex < C:
            if graph[ey][ex] in seti:
                continue
            seti.add(graph[ey][ex])
            recur(ey, ex, seti)
            seti.remove(graph[ey][ex])


R, C = map(int, input().split())
# 보드 정보
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

# 최대 개수를 저장할 변수 할당
result = 0
# dfs 탐색
recur(0, 0, set(graph[0][0]))

print(result)
"""

"""
20 20
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRST

20 20
ABCDEFGHIJKLMNOPQRST
BCDEFGHIJKLMNOPQRSTU
CDEFGHIJKLMNOPQRSTUV
DEFGHIJKLMNOPQRSTUVW
EFGHIJKLMNOPQRSTUVWX
FGHIJKLMNOPQRSTUVWXY
GHIJKLMNOPQRSTUVWXYZ
HIJKLMNOPQRSTUVWXYZZ
IJKLMNOPQRSTUVWXYZZZ
JKLMNOPQRSTUVWXYZZZZ
KLMNOPQRSTUVWXYZZZZZ
LMNOPQRSTUVWXYZZZZZZ
MNOPQRSTUVWXYZZZZZZZ
NOPQRSTUVWXYZZZZZZZZ
OPQRSTUVWXYZZZZZZZZZ
PQRSTUVWXYZZZZZZZZZZ
QRSTUVWXYZZZZZZZZZZZ
RSTUVWXYZZZZZZZZZZZZ
STUVWXYZZZZZZZZZZZZZ
TUVWXYZZZZZZZZZZZZZZ


20 20
ABZZZZZZZZZZZZZZZZZZ
BCDZZZZZZZZZZZZZZZZZ
ZDEFZZZZZZZZZZZZZZZZ
ZZFGHZZZZZZZZZZZZZZZ
ZZZHIJZZZZZZZZZZZZZZ
ZZZZJKLZZZZZZZZZZZZZ
ZZZZZLMNZZZZZZZZZZZZ
ZZZZZZNOPZZZZZZZZZZZ
ZZZZZZZPQRZZZZZZZZZZ
ZZZZZZZZRSTZZZZZZZZZ
ZZZZZZZZZTUVZZZZZZZZ
ZZZZZZZZZZVWXZZZZZZZ
ZZZZZZZZZZZXZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZZZZZZZZ



# bfs
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

visited = [[0 for _ in range(C)] for _ in range(R)]
route = [[[] for _ in range(C)] for _ in range(R)]

q = deque()
q.append([0, 0])
visited[0][0] = 1
route[0][0].append(graph[0][0])

while q:
    ny, nx = q.popleft()
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < R and 0 <= ex < C:
            if visited[ey][ex]:
                continue
            if graph[ey][ex] in route[ny][nx]:
                continue
            route[ey][ex] = route[ny][nx] + [graph[ey][ex]]
            visited[ey][ex] = 1
            q.append([ey, ex])

print(route)
result = 0
for y in range(R):
    for x in range(C):
        result = max(result, len(route[y][x]))

print(result)
"""