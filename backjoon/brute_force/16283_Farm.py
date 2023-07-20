# 16283번 Farm
# https://www.acmicpc.net/problem/16283

a, b, n, w = map(int, input().split())
result = []

# x : 양의 수
for x in range(1, 1000):
    if n-x > 0:
        if a * x + (n-x) * b == w:
            result.append(x)

if len(result) == 1:
    print(result[0], n-result[0])
else:
    print(-1)
