# 2613번 숫자구슬
# https://www.acmicpc.net/problem/2613

import sys

input = sys.stdin.readline


def split_group(g, m):
    # print(g, m)
    totals = [i[1] for i in g]
    group = [i[0] for i in g]
    if len(g) == M:
        return group
    goal = M - len(g)
    new_group = []

    if m not in totals:
        return 0
    target = -1
    c = int(1e9)
    for idx, total in enumerate(totals):
        if total == m:
            if c > group[idx]:
                c = group[idx]
                target = idx

    is_done = False
    # print("og group", group)
    for idx, cnt in enumerate(group):
        # print(idx, goal, "new_group", new_group)
        if idx == target or is_done:
            new_group.append(cnt)
            continue

        while goal and cnt > 1:
            new_group.append(1)
            cnt -= 1
            goal -= 1
        if goal == 0:
            is_done = True
        if cnt:
            new_group.append(cnt)
    # print("last new group", new_group)
    return new_group


def parametric_search():
    global result, result_arr

    start = max(marble)
    end = sum(marble)

    while start <= end:
        mid = (start + end) // 2
        group = []
        cnt_marble = 0
        total = 0
        for idx in range(N):
            if total + marble[idx] > mid:
                if total:
                    group.append([cnt_marble, total])
                cnt_marble = 1
                total = marble[idx]
            else:
                total += marble[idx]
                cnt_marble += 1
        else:
            if total:
                group.append([cnt_marble, total])

        # print("group", group)
        if len(group) <= M:
            end = mid - 1
            if result >= mid:
                g = split_group(group, mid)
                if g:
                    result = mid
                    result_arr = g

        else:
            start = mid + 1
        # print(start, end)
        # print(result, mid, len(group), result_arr)


N, M = map(int, input().split())
marble = list(map(int, input().split()))

result = sum(marble)
result_arr = []

parametric_search()
print(result)
print(*result_arr)

"""
input
8 3
5 4 2 6 9 3 8 7
output
17
4 2 2

input
9 6
1 1 1 1 1 1 1 1 1
output
2
1 1 2 2 2 1

input
6 4
1 1 1 4 1 1
output
4
1 2 1 2

input
2 1
1 1
output
2
2

input
4 4
4 3 2 1
output
4
1 1 1 1

input
7 3
1 1 1 1 17 18 23
output
23
5 1 1

input
4 4
1 1 2 1
output
2
1 1 1 1
"""