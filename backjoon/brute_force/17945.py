# 17945번 통학의 신
# https://www.acmicpc.net/problem/17945

A, B = map(int, input().split())
result = []
maxi = int(1000 ** (1/2))
for x in range(-maxi, maxi+1):
    if x**2 + 2 * A * x + B == 0:
        result.append(x)
print(*result)