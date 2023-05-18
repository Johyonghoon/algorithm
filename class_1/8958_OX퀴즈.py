# 8958번 OX퀴즈
# https://www.acmicpc.net/problem/8958

n = int(input())
for i in range(n):
    t = input()
    total, score = 0, 0
    for j in t:
        if j == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)
