# 2108번 통계학
# https://www.acmicpc.net/problem/2108
import sys
from collections import defaultdict, Counter
input = sys.stdin.readline


arr = []
d = defaultdict(int)

# N은 홀수
N = int(input())

for _ in range(N):
    arr.append(int(input()))

# 산술평균 : N개 수의 합을 N으로 나눈 값
print(round(sum(arr) / N))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
arr.sort()
print(arr[len(arr) // 2])

# 최빈값 : N개 수들 중 가장 많이 나타나는 값
cnt = Counter(arr).most_common()

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(arr) - min(arr))


"""
# 최빈값
for num in arr:
    d[num] += 1
result = []
for k, v in d.items():
    if v == max(d.values()):
        result.append(k)
if len(result) == 1:
    print(result[0])
else:
    print(sorted(result)[1])
"""