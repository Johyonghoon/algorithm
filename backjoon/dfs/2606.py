# 2606번 바이러스
# https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

# 연결 노드 확인하기
def recur(node):
    visited[node] = True
    for nxt in edges[node]:
        if visited[nxt]:
            continue
        recur(nxt)


computer = int(input())
E = int(input())
edges = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]
# 양방향 간선 정보 입력
for _ in range(E):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

recur(1)

cnt = -1  # 자기 자신을 방문하기 때문
for isTrue in visited:
    if isTrue:
        cnt += 1

print(cnt)