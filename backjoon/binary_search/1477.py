# 1477번 휴게소 세우기
# https://www.acmicpc.net/problem/1477

"""
# 이분탐색
"""
import heapq

N, M, L = map(int, input().split())
rests = [0, L] + list(map(int, input().split()))
rests.sort()
print(rests)

# N+2개의 지점을 가지고 있으므로, 거리는 N+1개 가지고 있다.
dist = []
for idx in range(N+1):
    dist.append(rests[idx+1]-rests[idx])
dist.sort(reverse=True)
print(dist)

# 이분탐색의 관점 : 목표점은 거리의 최소값
j = 0
start = 1
end = L-1
result = L
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    print(start, end, result)
    for i in range(N+1):
        cnt += (dist[i]-1) // mid
    if cnt <= M:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1
    # print(cnt)

print(result)
