# 11725번 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
import sys
# 재귀의 깊이 때문에 런타임에러 발생
sys.setrecursionlimit(10**9)


def recur(node, prv):
    # 부모 정보 저장
    prnt[node] = prv

    for nxt in tree[node]:
        # 만약 부모라면 탐색하지 않는
        if nxt == prv:
            continue
        recur(nxt, node)


N = int(input())
# 각 인덱스의 연결 정보를 저장
tree = [[] for _ in range(N+1)]
# 부모 정보 저장
prnt = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    # 양쪽에 연결 정보를 입력 해줘야 함
    tree[a].append(b)
    tree[b].append(a)
# node 1은 root로 부모가 없으니 0으로 없음을 나타냄
recur(1, 0)
[print(i) for i in prnt[2:]]
