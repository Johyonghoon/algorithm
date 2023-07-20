# 2164번 카드2
# https://www.acmicpc.net/problem/2164

N = int(input())
arr = [i for i in range(1, N+1)]

while len(arr) != 1:
    arr.pop(0)
    arr.append(arr[0])
    arr.pop(0)

print(*arr)
