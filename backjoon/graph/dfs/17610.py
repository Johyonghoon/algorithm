# 17610번 양팔저울
# https://www.acmicpc.net/problem/17610

"""
무게 추의 합, 차의 모든 경우의 수를 탐색
이때, 1에서 모든 추의 합인 S까지의 경우의 수만 탐색
"""


def dfs(node, total):
    if node == k:
        if 0 < total <= all:
            numbers.add(total)
        return

    dfs(node+1, total)
    dfs(node+1, total+weight[node])
    dfs(node+1, total-weight[node])


k = int(input())
weight = sorted(list(map(int, input().split())))
all = sum(weight)
numbers = set()
dfs(0, 0)
# print(numbers)
print(all - len(numbers))
