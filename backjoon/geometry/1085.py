# 1085번 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

# 각 변에 도달하는 거리
up = h - y
down = y
right = w - x
left = x

# 최대값은 1000
result = 1000
if result > up:
    result = up
if result > down:
    result = down
if result > left:
    result = left
if result > right:
    result = right

print(result)
