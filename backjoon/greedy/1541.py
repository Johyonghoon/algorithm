# 1541 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

arr = list(map(str, input().split('-')))
total = 0

for i, j in enumerate(arr):
    ls = list(map(int, j.split('+')))
    if i == 0:
        total = sum(ls)
    else:
        total -= sum(ls)

print(total)
