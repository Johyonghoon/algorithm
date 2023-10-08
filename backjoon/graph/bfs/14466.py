# 14466번 소가 길을 건너간 이유 6
# https://www.acmicpc.net/problem/14466

"""
N * N 의 목초지가 격자로 이루어져 있다.
인접한 목초지 사이는 일반적으로 자유롭게 건너갈 수 있지만, 일부는 길을 건너야 한다.
이때 2번째 줄부터 R개의 줄만큼 길에 대한 정보가 주어진다.
2 2 2 3 => (2, 2)~(2, 3)은 길로 연결되어 있다.

0 0 0
0 1-1
0 0 0

이때 배열의 좌표로 생각한다면 (1, 1) ~ (1, 2)가 길로 연결되어 있다는 뜻이다.
길이 없다면 인접한 배열 간에는 자유롭게 이동할 수 있으므로,
(1, 1)과 (1, 2)에 소가 존재한다고 가정하면
위와 같은 길만 존재한다면 다른 길로 돌아서 해당 좌표에 닿을 수 있다.
즉, 길을 이용하지 않더라도 만날 수 있다는 뜻이다.

"""
from collections import deque

N, K, R = map(int, input().split())

# 길에 대한 정보 입력 - 길로는 이동할 수 없다고 생각하자
edges = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    ay, ax, by, bx = map(lambda x: int(x)-1, input().split())
    edges[ay][ax].append([by, bx])
    edges[by][bx].append([ay, ax])

cows = []
for _ in range(K):
    cy, cx = map(lambda x: int(x)-1, input().split())
    cows.append([cy, cx])

# 모든 소에 대해 bfs 탐색
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = 0
for idx in range(K):
    q = deque()
    cy, cx = cows[idx]
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[cy][cx] = 1
    q.append([cy, cx])

    while q:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < N:
                # 길에 해당한다면 패스
                if [ey, ex] in edges[ny][nx]:
                    continue
                # 이미 방문했다면 패스
                if graph[ey][ex]:
                    continue
                graph[ey][ex] = 1
                q.append([ey, ex])

    cnt = K
    for fy, fx in cows:
        # 해당 좌표에 값을 가진다는 뜻은 길을 통하지 않고도 만날 수 있다는 뜻이다.
        # 자기 자신은 무조건 값을 가지고 있다.
        if graph[fy][fx]:
            cnt -= 1
    result += cnt

# 1번 소와 2번 소가 만나지 못한다면, 1번 소의 입장에서도, 2번 소의 입장에서도 각각 카운트 되기 때문에 나누기!
print(result // 2)
