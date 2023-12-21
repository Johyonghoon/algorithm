# 12837번 가계부(Hard)
# https://www.acmicpc.net/problem/12837

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def segment_tree(node, start, end):
    if start == end:
        tree[node] = io[start]
        return tree[node]
    mid = (start + end) // 2
    left_child = segment_tree(node*2, start, mid)
    right_child = segment_tree(node*2+1, mid+1, end)
    tree[node] = left_child + right_child
    return tree[node]


def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, diff)
    update(node*2+1, mid+1, end, idx, diff)


def calc(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_child = calc(node*2, start, mid, left, right)
    right_child = calc(node*2+1, mid+1, end, left, right)
    return left_child + right_child


N, Q = map(int, input().split())
io = [0 for _ in range(N+1)]
h = math.ceil(math.log2(N)) + 1
size = 1 << h
tree = [0 for _ in range(size)]
segment_tree(1, 0, N-1)

# print(tree)
for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        # c는 변화량 그 자체이므로 따로 차이를 반영하지 않는다.
        update(1, 0, N-1, b, c)
        io[b] = c
        # print('tree', tree)
        # print('io', io)
    elif a == 2:
        b -= 1
        c -= 1
        print(calc(1, 0, N-1, b, c))
