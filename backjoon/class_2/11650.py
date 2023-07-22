# 11650번 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in arr:
    print(*i)
