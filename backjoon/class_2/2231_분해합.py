# 2231번 분해합
# https://www.acmicpc.net/problem/2231

n = int(input())
ans = 0
for i in range(n-1, 0, -1):
    result = i
    x = i
    while x != 0:
        result += x % 10
        x = x // 10
    if result == n:
        ans = i

print(ans)
