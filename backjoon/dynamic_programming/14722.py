# 14722번 우유 도시
# https://www.acmicpc.net/problem/14722

"""
1. 맨 처음에는 딸기 우유를 한 팩 마신다.
2. 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
3. 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
4. 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다.

정사각형 2차원 격자 모양의 우유 가게들이 있을 때 왼쪽 위부터 오른쪽 아래까지 우유를 사마신다.
각각 우유 가게는 딸기, 초코, 바나나 중 한 종류의 우유만을 취급
영학이는 오직 동쪽 또는 남쪽으로만 움직이기 때문에 한 번 지나친 우유 가게는 다시 가지 않는다.
각각의 우유 가게 앞에서, 영학이는 우유를 사 마시거나, 사 마시지 않는다.
영학이가 마실 수 있는 최대 우유 개수?
좌표를 거슬러 올라가면서 각 좌표에서 출발했을 때 최대로 마실 수 있는 우유 개수 판단
0 : 딸기 / 1 : 초코 / 2 : 바나나
(N-1, N-1) 부터 거슬러 올라가기?
"""
import sys
input = sys.stdin.readline


def search():
    global result
    if graph[1][1] == 0:
        dp[1][1] = 1

    for y in range(1, N+1):
        for x in range(1, N+1):
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
            if dp[y][x] % 3 == graph[y][x]:
                dp[y][x] += 1
                result = max(result, dp[y][x])


delta = [[1, 0], [0, 1]]
N = int(input())
graph = [[0 for _ in range(N+1)]]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append([0] + arr)

result = 0
search()
# print(dp)
print(result)
