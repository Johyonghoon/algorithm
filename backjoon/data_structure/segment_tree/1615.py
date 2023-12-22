# 1615번 교차개수세기
# https://www.acmicpc.net/problem/1615

"""
출발 간선을 기준으로 정렬해서 이미 계산한 애들은 나보다 먼저 들어간,
즉 출발노드가 나보다 작은 애들이니까 도착 노드가 나보다 큰 경우를 카운트
"""

import sys
import math
input = sys.stdin.readline


def update(node, start, end, idx):
    if idx < start or end < idx:
        return
    tree[node] += 1
    if start == end:
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx)
    update(node*2+1, mid+1, end, idx)


def calc(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_child = calc(node*2, start, mid, left, right)
    right_child = calc(node*2+1, mid+1, end, left, right)
    return left_child + right_child


N, M = map(int, input().split())
h = math.ceil(math.log2(N)) + 1
size = 1 << h
tree = [0 for _ in range(size)]

edges = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if a not in edges:
        edges[a] = set()
    edges[a].add(b)

result = 0
for i in range(1, N+1):
    if i not in edges:
        continue
    for destination in sorted(edges[i]):
        update(1, 1, N, destination)
        result += calc(1, 1, N, destination+1, N)
        # print(index, result, tree)

print(result)
