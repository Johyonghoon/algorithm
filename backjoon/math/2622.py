# 2622번 삼각형만들기
# https://www.acmicpc.net/problem/2622

N = int(input())

cnt = 0
for x in range(1, N//3+1):
    for y in range((N-x)//2, x-1, -1):
        z = N - x - y
        if z < x + y:
            cnt += 1
        else:
            break

print(cnt)
