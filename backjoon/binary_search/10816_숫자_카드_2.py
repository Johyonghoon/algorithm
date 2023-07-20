# 10816번 숫자 카드 2
# https://www.acmicpc.net/problem/10816
import sys
from collections import defaultdict

input = sys.stdin.readline
d = defaultdict(int)

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_n:
    d[i] += 1

result = []
for j in arr_m:
    result.append(d[j])

print(*result)

