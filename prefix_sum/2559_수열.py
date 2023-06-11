# 2559번 수열
# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]

for i in range(1, n+1):
    prefix[i] = arr[i-1] + prefix[i-1]

result = []
for i in range(k, n+1):
    result.append(prefix[i] - prefix[i-k])

print(max(result))
