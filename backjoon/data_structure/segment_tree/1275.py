# 1275번 커피숍2
# https://www.acmicpc.net/problem/1275

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def segment_tree(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    mid = (start + end) // 2
    left_child = segment_tree(node*2, start, mid)
    right_child = segment_tree(node*2+1, mid+1, end)
    tree[node] = left_child + right_child
    return tree[node]


def calc(node, start, end, left, right):
    # 계산에 반영되지 않는 값
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_child = calc(node*2, start, mid, left, right)
    right_child = calc(node*2+1, mid+1, end, left, right)
    return left_child + right_child


def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, diff)
    update(node*2+1, mid+1, end, idx, diff)


def solve():
    for _ in range(Q):
        l, r, index, number = map(int, input().split())
        if l > r:
            l, r = r, l
        l, r, index = l-1, r-1, index-1
        print(calc(1, 0, N-1, l, r))
        update(1, 0, N-1, index, number - numbers[index])
        numbers[index] = number


if __name__ == '__main__':
    N, Q = map(int, input().split())
    numbers = list(map(int, input().split()))
    h = math.ceil(math.log2(N)) + 1
    size = 1 << h
    tree = [0 for _ in range(size)]
    segment_tree(1, 0, N-1)
    # print(tree)
    solve()
