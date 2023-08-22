# 11725번 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
# 재귀의 깊이로 인해 발생하는 런타임 에러를 방지
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, prv):

    prnts[node] = prv

    for nxt in edges[node]:
        # 이전으로 다시 거슬러 올라가지 않음
        if nxt == prv:
            continue
        recur(nxt, node)


# 정점-간선 정보 입력
N = int(input())
edges = [[] for _ in range(N+1)]
prnts = [0 for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    # 양방향
    edges[n1].append(n2)
    edges[n2].append(n1)

# 문제조건) root = 1, 루트는 부모가 없음
recur(1, 0)

# 문제조건) 2번 노드부터 부모 노드의 번호를 순서대로 출력
[print(prnts[i]) for i in range(2, N+1)]
