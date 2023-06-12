# 14719번 빗물
# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] + [i for i in arr]

if prefix.count(max(arr)) > 1:
    start = prefix.index(max(arr))
    prefix.reverse()
    end = W - prefix.index(max(arr))
    prefix.reverse()
    for i in range(start, end):
        prefix[i] = max(arr)

for i in range(W+1):
    if prefix[i] == max(arr):
        break
    prefix[i+1] = max(prefix[i], prefix[i+1])

for i in range(W, 0, -1):
    if prefix[i] == max(arr):
        break
    prefix[i-1] = max(prefix[i], prefix[i-1])

print(sum(prefix) - sum(arr))
