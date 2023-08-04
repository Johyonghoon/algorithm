# 2669번 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669

# 모든 x, y 좌표는 1 이상 100 이하의 정수
# 이에 맞는 그래프 정의 (0은 좌표에 없더라도 x,y 좌표를 생각하지 않기 위해 추가)
graph = [[False for _ in range(101)] for _ in range(101)]

# 중복되는 면적을 제외하기 위해 이미 True 라면 의미없게 만들어 줌
for _ in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())
    for ey in range(ldy, ruy):
        for ex in range(ldx, rux):
            graph[ey][ex] = True

area = 0
for y in range(101):
    for x in range(101):
        if graph[y][x]:
            area += 1

print(area)
