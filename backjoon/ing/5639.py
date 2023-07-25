# 5639번 이진 검색 트리
# https://www.acmicpc.net/problem/5639

import sys

lines = sys.stdin.readlines()
tree = [[0, 0] for _ in range(10 ** 6 + 1)]
for idx in range(len(lines)):
    lines[idx] = int(lines[idx].replace("\n", ""))
