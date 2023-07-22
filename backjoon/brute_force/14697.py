# 14697번 방 배정하기
# https://www.acmicpc.net/problem/14697

A, B, C, N = map(int, input().split())
result = 0

for a in range(N//A+1):
    for b in range(N//B+1):
        for c in range(N//C+1):
            if a * A + b * B + c * C == N:
                result = 1
                break
            if a * A + b * B + c * C > N:
                break
        if result == 1:
            break
    if result == 1:
        break

print(result)