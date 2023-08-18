# 17608번 막대기
# https://www.acmicpc.net/problem/17608
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 최대값이 갱신될 때마다 개수 추가
maxi = 0
cnt = 0
for height in arr[::-1]:
    if maxi < height:
        maxi = height
        cnt += 1

print(cnt)
