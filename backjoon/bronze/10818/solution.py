# 10818번 최소, 최대
# https://www.acmicpc.net/problem/10818
import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
# 내장함수 min, max 지양하기
# 모든 수를 정렬할 필요 없이 가장 큰 수와 작은 수를 찾기
mini = 1_000_000
maxi = -1_000_000

for number in arr:
    if mini > number:
        mini = number
    if maxi < number:
        maxi = number

print(mini, maxi)
