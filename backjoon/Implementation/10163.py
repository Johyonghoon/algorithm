# 10163번 색종이
# https://www.acmicpc.net/problem/10163
import sys
input = sys.stdin.readline

graph = [[True for _ in range(1001)] for _ in range(1001)]
N = int(input())
# 가장 마지막의 색종이 정보부터 탐색
# 이미 탐색되었던 좌표라면 색종이가 설치되지 않는 것으로 판단
papers = []
for idx in range(1, N+1):
    x, y, width, height = map(int, input().split())
    papers.append((x, y, width, height))

rev_result = []
for paper in papers[::-1]:
    x, y, width, height = paper
    cnt = 0
    for ey in range(y, y+height):
        for ex in range(x, x+width):
            if graph[ey][ex]:
                cnt += 1
                graph[ey][ex] = False
    rev_result.append(cnt)

result = reversed(rev_result)
[print(i) for i in result]
