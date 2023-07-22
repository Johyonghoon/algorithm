# 7568번 덩치
# https://www.acmicpc.net/problem/7568

N = int(input())
arr = []
result = []
for _ in range(N):
    weight, height = map(int, input().split())
    arr.append((weight, height))

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    result.append(rank)

print(*result)