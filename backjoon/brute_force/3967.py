# 3967번 매직 스타
# https://www.acmicpc.net/problem/3967

"""
완전탐색 시도
좌표 순서 미리 구하기


"""


def magic_star(n):
    graph = [["." for _ in range(9)] for _ in range(5)]
    idx = 0
    for k, coordinate in enumerate(coor):
        ny, nx = coordinate
        graph[ny][nx] = chr(ord("A") + n[k] - 1)

    [print("".join(i)) for i in graph]


def dfs(idx):
    global is_true

    if idx == 12:
        for coordinate in magic:
            total = 0
            for j in coordinate:
                total += num[j]
            if total != 26:
                return
        magic_star(num)
        is_true = True
        return

    if num[idx] != -1:
        dfs(idx+1)
        return

    for number in range(1, 13):
        if is_true:
            break
        if visited[number]:
            continue
        num[idx] = number
        visited[number] = 1
        dfs(idx+1)
        visited[number] = 0
        num[idx] = -1


coor = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7),
        (2, 2), (2, 6), (3, 1), (3, 3), (3, 5),
        (3, 7), (4, 4)]

magic = [[0, 2, 5, 7],
         [1, 2, 3, 4],
         [0, 3, 6, 10],
         [7, 8, 9, 10],
         [1, 5, 8, 11],
         [4, 6, 9, 11]]

num = []
visited = [0 for _ in range(13)]
visited[0] = 1
for _ in range(5):
    arr = list(input())
    for c in arr:
        if c != ".":
            if c == "x":
                num.append(-1)
                continue

            num.append(ord(c) - ord("A") + 1)
            visited[num[-1]] = 1

is_true = False
dfs(0)
