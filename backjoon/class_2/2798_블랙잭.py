# 2798번 블랙잭
# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = arr[i] + arr[j] + arr[k]
            if total <= m and total > result:
                result = total

print(result)
