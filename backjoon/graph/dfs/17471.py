# 17471번 게리맨더링
# https://www.acmicpc.net/problem/17471

import sys
input = sys.stdin.readline


def recur(node, arr):
    visited[node] = 1
    for nxt in edges[node]:
        if nxt not in arr:
            continue
        if visited[nxt]:
            continue
        recur(nxt, arr)


def grouping(node, arr1, arr2):
    global result, visited

    if len(arr1) == N or len(arr2) == N:
        return

    if len(arr1) + len(arr2) == N:
        visited = [0 for _ in range(N)]
        recur(arr1[0], arr1)
        recur(arr2[0], arr2)
        if 0 in visited:
            return
        else:
            total1 = 0
            total2 = 0
            for i in arr1:
                total1 += people[i]
            for i in arr2:
                total2 += people[i]
            result = min(result, abs(total2 - total1))

    for nxt in range(node+1, N):
        arr1.append(nxt)
        grouping(nxt, arr1, arr2)
        arr1.pop()
        arr2.append(nxt)
        grouping(nxt, arr1, arr2)
        arr2.pop()


N = int(input())
people = list(map(int, input().split()))
edges = []
for idx in range(N):
    arr = list(map(int, input().split()))
    if arr[0]:
        ls = [i-1 for i in arr[1:]]
        edges.append(ls)
    else:
        edges.append([])

result = 1001
grouping(-1, [], [])
if result == 1001:
    print(-1)
else:
    print(result)
