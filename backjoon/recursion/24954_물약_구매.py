# 24954번 물약 구매
# https://www.acmicpc.net/problem/24954
import sys

input = sys.stdin.readline

N = int(input())
cost = list(map(int, input().split()))
discount = [[] for _ in range(N)]
arr = [i for i in range(N)]
ls = []
result = int(1e9)

for i in range(N):
    p = int(input())
    for _ in range(p):
        dis_num, dis_price = map(int, input().split())
        discount[i].append((dis_num-1, dis_price))

def recur(price):
    global result
    if price > result:
        return

    if len(ls) == N:
        result = min(result, price)
        return

    for i in arr:
        if i in ls:
            continue
        ls.append(i)
        if discount[i]:
            for dis_num, dis_price in discount[i]:
                cost[dis_num] -= dis_price
        if cost[i] < 0:
            recur(price+1)
        else:
            recur(price+cost[i])
        if discount[i]:
            for dis_num, dis_price in discount[i]:
                cost[dis_num] += dis_price
        ls.pop()

recur(0)

print(result)

"""
import sys

input = sys.stdin.readline

N = int(input())
cost = list(map(int, input().split()))
discount = [[] for _ in range(N)]
arr = [i for i in range(N)]
ls = []
result = []

for i in range(N):
    p = int(input())
    for _ in range(p):
        dis_num, dis_price = map(int, input().split())
        discount[i].append((dis_num-1, dis_price))

def recur(price):
    if len(ls) == N:
        result.append(price)
        return
    for i in arr:
        if i in ls:
            continue
        ls.append(i)
        if discount[i]:
            for dis_num, dis_price in discount[i]:
                cost[dis_num] -= dis_price
        if cost[i] < 0:
            recur(price+1)
        else:
            recur(price+cost[i])
        if discount[i]:
            for dis_num, dis_price in discount[i]:
                cost[dis_num] += dis_price
        ls.pop()

recur(0)

print(min(result))
"""