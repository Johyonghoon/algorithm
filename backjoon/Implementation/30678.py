# 30678번 별 안에 별 안에 별 찍기
# https://www.acmicpc.net/problem/30678

"""
재귀 별찍기 문제
"""


def print_blank(idx):
    if idx == 0:
        print(" ")
        return
    for y in range(5):
        for x in range(5):
            print_blank(idx-1)


def print_star(idx, ny, nx):
    if idx == 0:
        graph[ny][nx] = "*"
        return

    for y, row in enumerate(stars):
        for x, column in enumerate(row):
            if column == "*":
                print_star(idx-1, ny*5+y, nx*5+x)


N = int(input())
graph = [[" " for _ in range(5**N)] for _ in range(5**N)]
stars = ["  *  ",
         "  *  ",
         "*****",
         " *** ",
         " * * "]

print_star(N, 0, 0)
[print("".join(i)) for i in graph]
