# 1932번 정수 삼각형
# https://www.acmicpc.net/problem/1932


def recur(n):
    global visited
    pass


n = int(input())
tri = []
visited = [[0 for _ in range(i)] for i in range(n)]
for _ in range(n):
    tri.append(list(map(int, input().split())))

print(visited)
print(tri)
recur(0)