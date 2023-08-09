# 1100번 하얀 칸
# https://www.acmicpc.net/problem/1100

# 체스판 그리기 // 하얀 칸을 True 로 설정
chess = [[False for _ in range(8)] for _ in range(8)]
for y in range(8):
    for x in range(8):
        if (y + x) % 2 == 0:
            chess[y][x] = True

# 체스 말 탐색
cnt = 0
for y in range(8):
    arr = list(input())
    for x, piece in enumerate(arr):
        if piece == "F":
            if chess[y][x]:
                cnt += 1

print(cnt)
