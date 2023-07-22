# 4153번 직각삼각형
# https://www.acmicpc.net/problem/4153

while True:
    arr = sorted(list(map(int, input().split())))
    if sum(arr) == 0:
        break
    else:
        if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
            print("right")
        else:
            print("wrong")
