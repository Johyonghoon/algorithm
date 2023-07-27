# 18870번 좌표 압축
# https://www.acmicpc.net/problem/18870
import sys
from collections import defaultdict
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

# 배열을 중복을 없앤 후 다시 배열로 만들어 정렬
d = defaultdict()
not_dup_arr = sorted(list(set(arr)))
# 그 리스트에 대해 인덱스를 활용하여 작은 수부터 좌표를 부여
for i, num in enumerate(not_dup_arr):
    d[num] = i

# 각 위치의 값들에 대해 인덱스 값을 부여하여 좌표 압축
result = [0 for _ in range(N)]
for idx, num in enumerate(arr):
    result[idx] = d[num]

print(*result)
