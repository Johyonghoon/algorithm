# 1037번 약수
# https://www.acmicpc.net/problem/1037

cnt = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0] * arr[-1])
