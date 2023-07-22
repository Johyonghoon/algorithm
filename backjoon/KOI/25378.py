# 25378번 조약돌
# https://www.acmicpc.net/problem/25378

N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for idx in range(1, N):
    if arr[idx] >= arr[idx-1] + arr[idx+1]:
        arr[idx] -= arr[idx-1] + arr[idx+1]
        arr[idx-1] = 0
        arr[idx+1] = 0
        cnt += 2
    if arr[idx] < arr[idx-1] + arr[idx+1]:
        if arr[idx-1] < arr[idx+1]:
            pass
        if arr[idx] < arr[idx-1] and arr[idx] < arr[idx+1]:
            pass



"""
1 5 1 8 10
"""