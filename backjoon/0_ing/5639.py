# 5639번 이진 검색 트리
# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node):
    global idx
    nodes[idx] = node



# 전위 순회로 정렬된 배열 생성하기
numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

N = len(numbers)
nodes = [0 for _ in range(N+1)]
tree = [[0, 0] for _ in range(N+1)]

nodes[1] = numbers[0]
j = 1       # 전위 순회로 정렬된 배열
idx = 1     # 노드

for i in range(2, N+1):
    for j in range(1, i):
        pass

