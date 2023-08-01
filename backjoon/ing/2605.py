# 2605번 줄 세우기
# https://www.acmicpc.net/problem/2605

N = int(input())
arr = list(map(int, input().split()))
line = []

for idx in range(N):
    line.insert(arr[idx], idx+1)

line.reverse()
print(*line)
