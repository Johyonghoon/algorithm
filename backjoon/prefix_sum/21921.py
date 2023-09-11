# 21921번 블로그
# https://www.acmicpc.net/problem/21921

"""
누적합
"""

N, X = map(int, input().split())
visit = list(map(int, input().split()))

for idx in range(1, N):
    visit[idx] += visit[idx-1]

result = [0 for _ in range(N)]
for idx in range(N):
    if idx < X:
        result[idx] = visit[idx]
        continue
    result[idx] = visit[idx] - visit[idx-X]

if max(result):
    print(max(result))
    print(result.count(max(result)))
else:
    print("SAD")
