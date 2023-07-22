# 2562번 최댓값
# https://www.acmicpc.net/problem/2562

ls = []
while len(ls) != 9:
    ls.append(int(input()))
print(max(ls))
print(ls.index(max(ls)) + 1)
