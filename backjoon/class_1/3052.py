# 3052번 나머지
# https://www.acmicpc.net/problem/3052

from collections import defaultdict

d = defaultdict(int)

for _ in range(10):
    d[int(input()) % 42] += 1

print(len(d))
