# 24041번 성싶당 밀키트
# https://www.acmicpc.net/problem/24041

"""
밀키트 N개의 재료의 i번째 재료는 구매 후 Li까지의 유통기한, 부패 속도는 Si
이때 구매 후 x일에 i번째 재료에 있는 세균 수는
Si * max(1, x-Li)
N개의 재료, K개까지 빼서 세균수가 G마리 이하라면 먹기로 했다.
밀키트를 산 날부터 며칠 후까지 먹을 수 있을까?
"""

import sys
import heapq
input = sys.stdin.readline


def parametric_search():
    global result
    start = 0
    end = tmp * 2
    while start <= end:
        mid = (start + end) // 2
        total = 0
        pq = []
        for o, s, l in ingr:
            if not o:
                total += s * max(1, mid-l)
            else:
                heapq.heappush(pq, -(s * max(1, mid-l)))

        for _ in range(K):
            if not pq:
                break
            heapq.heappop(pq)
        total += -sum(pq)

        if total <= G:
            result = max(result, mid)
            start = mid + 1
        else:
            end = mid - 1

        # print(mid, total, G)


N, G, K = map(int, input().split())
ingr = []
tmp = 0
for _ in range(N):
    S, L, O = map(int, input().split())
    tmp = max(tmp, L)
    ingr.append([O, S, L])

result = 0
parametric_search()

print(result)
