# 11505번 구간 곱 구하기
# https://www.acmicpc.net/problem/11505

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def segment_tree(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]

    mid = (start + end) // 2
    left_child = segment_tree(node * 2, start, mid)
    right_child = segment_tree(node * 2 + 1, mid+1, end)
    tree[node] = left_child * right_child % 1_000_000_007
    return tree[node]


def update(node, start, end, idx, num):
    if idx < start or end < idx:
        return tree[node]
    if start == end:
        tree[node] = num
        return num
    mid = (start + end) // 2
    left_child = update(node * 2, start, mid, idx, num)
    right_child = update(node * 2 + 1, mid+1, end, idx, num)
    tree[node] = left_child * right_child % 1_000_000_007
    return tree[node]


def calc(node, start, end, left, right):
    if end < left or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_child = calc(node*2, start, mid, left, right)
    right_child = calc(node*2+1, mid+1, end, left, right)
    return left_child * right_child % 1_000_000_007


N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
# print("numbers :", numbers)
h = math.ceil(math.log2(N)) + 1
size = 1 << h
tree = [0 for _ in range(size)]
segment_tree(1, 0, N-1)
# print('tree :', tree)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        update(1, 0, N-1, b, c)
        numbers[b] = c
        # print("changed numbers :", numbers)
        # print("changed tree :", tree)
    elif a == 2:
        b -= 1
        c -= 1
        print(calc(1, 0, N-1, b, c))
