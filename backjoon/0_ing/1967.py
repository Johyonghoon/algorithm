# 1967번 트리의 지름
# https://www.acmicpc.net/problem/1967

def recur(node):
    global maxi
    ls = []
    for nxt, length in tree[node]:
        recur(nxt)
        longest[node] = max(longest[node], length + longest[nxt])
        ls.append(length)

    if len(ls) > 1:
        ls.sort(reverse=True)
        maxi = max(maxi, sum(ls[:2]))

n = int(input())
tree = [[] for _ in range(n+1)]
longest = [0 for _ in range(n+1)]
maxi = 0
for _ in range(n-1):
    prnt, child, weight = map(int, input().split())
    tree[prnt].append((child, weight))

recur(1)

print(longest)
print(maxi)