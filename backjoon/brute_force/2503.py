# 2503번 숫자 야구
# https://www.acmicpc.net/problem/2503

n = int(input())
arr = []
result = 0
for i in range(n):
    ans, strike, ball = map(int, input().split())
    arr.append([ans, strike, ball])

# 완전 탐색
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b and a != c and b != c:
                cnt_case = 0
                for i in range(n):
                    ans, strike, ball = arr[i]
                    cnt_strike, cnt_ball = 0, 0
                    x = ans // 100
                    y = ans // 10 % 10
                    z = ans % 10
                    if a == x: cnt_strike += 1
                    if a == y or a == z: cnt_ball += 1
                    if b == y: cnt_strike += 1
                    if b == x or b == z: cnt_ball += 1
                    if c == z: cnt_strike += 1
                    if c == x or c == y: cnt_ball += 1
                    if cnt_strike == strike and cnt_ball == ball: cnt_case += 1
                    if cnt_case == n: result += 1

print(result)

"""
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
"""