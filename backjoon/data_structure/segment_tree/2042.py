# 2042번 구간 합 구하기
# https://www.acmicpc.net/problem/2042

"""
segment tree
중간에 수의 변경이 빈번히 일어나고, 그 중간에 어떤 부분의 합
"""

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def segment_tree(idx, start, end):
    if start == end:
        tree[idx] = numbers[start]
        return tree[idx]
    mid = (start + end) // 2
    left_child = segment_tree(idx * 2, start, mid)
    right_child = segment_tree(idx * 2 + 1, mid+1, end)
    tree[idx] = left_child + right_child
    return tree[idx]


def change_number(node, start, end, idx, diff):
    # 해당 범위 바깥의 경우 패스
    if idx < start or end < idx:
        return
    tree[node] += diff
    # 리프노드라면 돌아가기
    if start == end:
        return
    mid = (start + end) // 2
    change_number(node * 2, start, mid, idx, diff)
    change_number(node * 2+1, mid+1, end, idx, diff)


def total(idx, start, end, left, right):
    # 범위 바깥의 경우 더하지 않기
    if left > end or right < start:
        return 0
    # 범위 안에 들어갈 경우 값 리턴
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    left_child = total(idx * 2, start, mid, left, right)
    right_child = total(idx * 2 + 1, mid+1, end, left, right)
    return left_child + right_child


N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
# print('numbers', numbers)
h = math.ceil(math.log2(N)) + 1
size = 1 << h
tree = [0 for _ in range(size)]
segment_tree(1, 0, N-1)
# print('tree', tree)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 수를 c로 변경
        b -= 1
        # print('number, c', numbers[b], c)
        difference = c - numbers[b]
        numbers[b] = c
        change_number(1, 0, N-1, b, difference)
    elif a == 2:  # b번째 수부터 c번째 수까지의 합을 구하기
        b -= 1
        c -= 1
        print(total(1, 0, N-1, b, c))
