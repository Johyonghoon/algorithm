# 1991번 트리 순회
# https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline


# 전위 순회
def pre_order(node):
    if node == ord("."):
        return

    print(chr(node), end="")
    pre_order(tree[node][0])
    pre_order(tree[node][1])


# 중위 순회
def in_order(node):
    if node == ord("."):
        return

    in_order(tree[node][0])
    print(chr(node), end="")
    in_order(tree[node][1])


# 후위 순회
def post_order(node):
    if node == ord("."):
        return

    post_order(tree[node][0])
    post_order(tree[node][1])
    print(chr(node), end="")


N = int(input())
tree = [[] for _ in range(ord("Z")+1)]
for _ in range(N):
    a, b, c = map(ord, input().strip().split())
    tree[a].append(b)
    tree[a].append(c)

pre_order(ord("A"))
print()
in_order(ord("A"))
print()
post_order(ord("A"))


