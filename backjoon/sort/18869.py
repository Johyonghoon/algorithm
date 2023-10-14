# 18869번 멀티버스 2
# https://www.acmicpc.net/problem/18869

"""
M개의 우주에 각각 N개의 행성을 가지고 있다.
(?) 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다.
두 우주에 대해 모든 행성의 크기가 1 <= i, j < N 에 대해서 다음과 같은 조건을 만족 한다면, 두 우주를 균등하다고 한다.
Ai < Aj -> Bi < Bj
Ai == Aj -> Bi == Bj
Ai > Aj -> Bi > Bj
즉, 한 우주에 가지는 행성의 크기에 따른 순번을 따졌을 때, 그 순번이 같으면 균등한 우주

1 3 2       => 행성의 크기 순서 : 1 3 2
12 50 31    => 행성의 크기 순서 : 1 3 2
두 우주는 균등하다

# 시간초과
균등한 우주의 개수 중 2개를 뽑는 조합을 선택하면 균등한 우주의 쌍의 개수를 구할 수 있다.
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

M, N = map(int, input().split())
d = defaultdict(int)
for _ in range(M):
    # 행성의 순번 매기기
    wzu = list(map(int, input().split()))
    # 중복 수 제거
    sorted_wzu = sorted(list(set(wzu)))
    ranks = {sorted_wzu[rank]: rank for rank in range(len(sorted_wzu))}
    # 리스트(mutable)는 딕셔너리의 값이 될 수 없지만 튜플(iterable)은 가능하다.
    ranked_wzu = tuple([ranks[i] for i in wzu])
    d[ranked_wzu] += 1

result = 0
for cnt in d.values():
    result += cnt * (cnt-1) // 2

print(result)
