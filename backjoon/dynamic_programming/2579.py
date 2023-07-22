# 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])
else:
    d = [0 for _ in range(n + 1)]
    d[1:3] = [arr[1], arr[1]+arr[2]]

    for i in range(3, n+1):
        if d[i] != 0:
            continue
        d[i] = max(d[i-3] + arr[i-1], d[i-2]) + arr[i]
    print(d[n])

"""
10 20 15 25 10 20


"""