# 2304번 창고 다각형
# https://www.acmicpc.net/problem/2304

coordinate = []
n = int(input())
for i in range(n):
    L, H = map(int, input().split())
    coordinate.append([L, H])
coordinate.sort()
prefix = [0 for _ in range(coordinate[-1][0]+1)]

for L, H in coordinate:
    prefix[L] = H

if prefix.count(max(prefix)) > 1:
    start = prefix.index(max(prefix))
    prefix.reverse()
    end = len(prefix) - prefix.index(max(prefix))
    prefix.reverse()
    for L in range(start, end):
        prefix[L] = max(prefix)

for L, H in enumerate(prefix):
    if H == max(prefix):
        break
    prefix[L+1] = max(prefix[L], prefix[L+1])

prefix.reverse()
for L, H in enumerate(prefix):
    if H == max(prefix):
        break
    prefix[L+1] = max(prefix[L], prefix[L+1])

print(sum(prefix))
