# 9095번 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

t = int(input())
d = [1 for _ in range(11)]
while t != 0:
    n = int(input())
    d[1:3] = [2, 4]
    for i in range(3, n):
        if d[i] != 1:
            continue
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n-1])
    t -= 1

