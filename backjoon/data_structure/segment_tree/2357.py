# 2357번 최솟값과 최댓값
# https://www.acmicpc.net/problem/2357

"""
세그먼트 트리 연습문제
여러 개의 데이터가 존재할 때 특정 구간의 합(최솟값, 최댓값, 곱 등)을 구하는 데 사용하는 자료구조
"""

import sys
import math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


# 세그먼트 트리 구성하기
def segment_tree(start, end, idx):
    # 리프노드에 도달했을 때
    if start == end:
        # 자기 자신의 최소, 최대값으로 가짐
        tree[idx] = (numbers[start], numbers[start])
        return tree[idx]
    mid = (start + end) // 2
    left_child = segment_tree(start, mid, idx * 2)
    right_child = segment_tree(mid+1, end, idx * 2 + 1)
    tree[idx] = (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))
    return tree[idx]


# 범위 안의 값 중 최소, 최대값 탐색하기
# numbers 범위 : start, end / tree 인덱스 : idx / 범위 : left, right
def search(start, end, idx):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return (int(1e9)+1, 0)   # 절대 계산에 반영되지 않을 배열 리턴
    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return tree[idx]
    # 그렇지 않다면 최소, 최대 탐색
    mid = (start + end) // 2
    left_node = search(start, mid, idx * 2)
    right_node = search(mid+1, end, idx * 2 + 1)
    return (min(left_node[0], right_node[0]), max(left_node[1], right_node[1]))


N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

# 세그먼트 트리의 크기 : 배열의 개수가 N일 때 N보다 큰 가장 가까운 제곱수 * 2
# h = math.ceil(math.log2(N)) + 1
# size = 1 << h
h = math.ceil(N**(1/2)) + 1
size = h ** 2 * 2
tree = [0 for _ in range(size)]
segment_tree(0, N-1, 1)
# print(tree)

for _ in range(M):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    print(*search(0, N-1, 1))
