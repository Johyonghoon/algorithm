# 17085번 십자가 2개 놓기
# https://www.acmicpc.net/problem/17085

"""
# 위치에만 십자가가 위치할 수 있다.
하지만 경계선에 있는 위치에 십자가 중심이 위치한다면 길이가 0,
즉, 면적이 1만 될 수 있으므로 탐색하지 않는다.
경계선에만 위치할 수 있다면 결과는 1 * 1 이므로 최소 결과를 1로 둔다.
"""


def cnt_cross(x):
    return 4 * x + 1


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cross = [[0 for _ in range(M)] for _ in range(N)]
result = 1  # 1 * 1

# d의 범위는 정 가운데를 기준으로 짧은 변의 길이의 반보다 1만큼 긴 길이이다.
scope = 0
if N >= M:
    scope = M // 2 + 1
else:
    scope = N // 2 + 1

# 십자가가 1 이상의 길이를 가지는 경우 추가
available_ls = []
# 각 좌표의 최대 십자가 크기 구하기
for y in range(1, N-1):
    for x in range(1, M-1):
        if graph[y][x] == "#":
            breaky = False
            for d in range(1, scope):
                if breaky:
                    break
                for dy, dx in delta:
                    ey = y + dy * d
                    ex = x + dx * d
                    if ey < 0 or ey >= N or ex < 0 or ex >= M:
                        breaky = True
                        break
                    if graph[ey][ex] != "#":
                        breaky = True
                        break
                else:
                    cross[y][x] = d
            if cross[y][x]:
                available_ls.append([y, x])
        else:
            cross[y][x] = -1
#
# if len(available_ls) == 0:
#     print(1)
# elif len(available_ls) == 1:
#     ny, nx = available_ls[0]
#     print(cnt_cross(cross[ny][nx]))
# else:
for i in range(len(available_ls)):
    ay, ax = available_ls[i]
    result = max(result, cnt_cross(cross[ay][ax]))
    for j in range(i, len(available_ls)):
        if i == j:
            continue
        test_cross = [[0 for _ in range(M)] for _ in range(N)]
        by, bx = available_ls[j]
        for a in range(cross[ay][ax]+1):
            breaky = False
            for dy, dx in delta:
                ey, ex = ay + dy * a, ax + dx * a
                test_cross[ey][ex] += 1
            else:
                for b in range(cross[by][bx]+1):
                    if breaky:
                        break
                    for ddy, ddx in delta:
                        eey, eex = by + ddy * b, bx + ddx * b
                        if test_cross[eey][eex]:
                            breaky = True
                            break
                    else:
                        result = max(result, cnt_cross(a) * cnt_cross(b))

print(result)
