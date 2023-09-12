# A와 B 2
# https://www.acmicpc.net/problem/12919

"""
S to T 는 문자를 더하면서 너무 많은 경우의 수가 발생
T to S 를 통해 문자를 빼며 조건을 만족하는 경우에만 탐색
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, arr):
    global isTrue
    if isTrue:
        return

    if node == L:
        # print(arr, S)
        if arr == S:
            isTrue = True
        return

    if arr[-1] == "A":
        arr.pop()
        recur(node-1, arr)
        arr.append("A")

    if arr[0] == "B":
        arr.reverse()
        arr.pop()
        recur(node-1, arr)
        arr.append("B")
        arr.reverse()


S = list(input().strip())
T = list(input().strip())

L = len(S)
isTrue = False
recur(len(T), T)

print(int(isTrue))
