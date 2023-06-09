# 2503번 숫자 야구
# https://www.acmicpc.net/problem/2503

arr = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                arr.append((i, j, k))

n = int(input())
for _ in range(n):
    ls = []
    ans, strike, ball = map(int, input().split())
    ans = tuple(map(int, str(ans)))
    for i in arr:
        cnt_strike, cnt_ball = 0, 0
        for j in range(3):
            if i[j] == ans[j]:
                cnt_strike += 1
            for k in range(3):
                if j != k and i[j] == ans[k]:
                    cnt_ball += 1
        if strike != cnt_strike or ball != cnt_ball:
            ls.append(i)
    for i in ls:
        arr.remove(i)

print(len(arr))
