# 11724번 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline
# 재귀의 깊이 때문에 런타임 에러 발생
sys.setrecursionlimit(1_000_000_000)


# 방문 노드에 부모 노드를 기록하여, 연결되어 있는 모든 노드의 루트 노드 확인
# 루트 노드의 개수를 파악하면 문제를 해결할 수 있음
def recur(node):
    visited[node] = True

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        prnt[nxt] = prnt[node]
        recur(nxt)


# 간선 정보 입력
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
prnt = [i for i in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

# 전체 노드에 대해 부모 탐색
for nd in range(1, N+1):
    if visited[nd]:
        continue
    recur(nd)

# 중복을 제거하여 개수 출력
cnt = set(prnt[1:])
print(len(cnt))
