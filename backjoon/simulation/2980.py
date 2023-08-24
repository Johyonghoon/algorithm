# 2980번 도로와 신호등
# https://www.acmicpc.net/problem/2980

"""
0. 1초에 1미터 이동
1. 신호등을 지나며, 도로의 끝까지 이동하는 데 걸리는 시간
"""


N, L = map(int, input().split())
rgb = []
for _ in range(N):
    D, R, G = map(int, input().split())
    rgb.append([D, R, G])

# 거리 순 정렬
rgb.sort()

sec = 0
location = 0
while location < L:
    # 지나가야 하는 신호등이 있을 때
    if rgb:
        arr = rgb.pop(0)
        dist, red, green = arr
        # 신호등 위치까지 이동
        while location < dist:
            location += 1
            sec += 1
        # 신호를 통과할 때까지 기다리기
        while not red <= sec % (red+green) < red+green:
            sec += 1
        location += 1
        sec += 1

    # 지나가야 하는 신호등이 없을 떄
    else:
        sec += 1
        location += 1

print(sec)
