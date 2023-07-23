# 15681번 트리와 쿼리
# https://www.acmicpc.net/problem/15681
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, prv):

    for nxt in tree[node]:
        if nxt == prv:
            continue
        recur(nxt, node)
        child[node] += 1

    # 부모에게 자식 개수를 넘겨 줌
    child[prv] += child[node]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
child = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

recur(R, 0)

for _ in range(Q):
    U = int(input())
    # 본인을 포함하기 위해 1 추가
    print(child[U] + 1)
