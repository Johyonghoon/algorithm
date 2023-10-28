# 1915번 가장 큰 정사각형
# https://www.acmicpc.net/problem/1915

"""
인덱스 탐색으로 가로 길이를 먼저 탐색한 다음...
"""


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

