n, m = map(int, input().split())
array = sorted([int(input()) for _ in range(n)])
d = [0] + [10001 for _ in range(m)]

for i in range(1, m+1):
    for j in array:
        if d[i-j] <= 10000:
            d[i] = min(d[i], d[i-j] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
