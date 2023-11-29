# 14725번 개미굴
# https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline


def dfs(idx, target):

    for k in sorted(list(target.keys())):
        print(f"{'--'*idx}{k}")
        dfs(idx+1, target[k])


trie = dict()
N = int(input())
for _ in range(N):
    arr = list(input().strip().split())
    cnt = int(arr[0])
    eats = arr[1:]
    target = trie
    for i in range(cnt):
        if eats[i] not in target:
            target[eats[i]] = dict()
        target = target[eats[i]]

# print(trie)
dfs(0, trie)
