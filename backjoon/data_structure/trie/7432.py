# 7432번 디스크 트리
# https://www.acmicpc.net/problem/7432

import sys
input = sys.stdin.readline


def dfs(idx, t):

    for k in sorted(t.keys()):
        print(f"{' '*idx}{k}")
        dfs(idx+1, t[k])


N = int(input())
trie = dict()
for _ in range(N):
    arr = list(input().strip().split('\\'))
    target = trie
    for i in range(len(arr)):
        if arr[i] not in target:
            target[arr[i]] = dict()
        target = target[arr[i]]

# print(trie)
dfs(0, trie)

