# 10653번 마라톤 2
# https://www.acmicpc.net/problem/10653

"""
https://magentino.tistory.com/163 풀이 참조
점프하는 경우를 필터링하면서 카운트하고 싶었는데 이상하게 잘 안되서 참고하고 풀게 됨 ㅠ
"""
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((y, x))

dp = [[int(1e9) for _ in range(K+1)] for _ in range(N)]
dp[0][-1] = 0
for i in range(N-1):
    for j in range(K+1):
        if dp[i][j] == int(1e9):
            continue
        for k in range(j+1):
            if i+k+1 >= N:
                break
            y2, x2 = coordinate[i+k+1]
            y1, x1 = coordinate[i]
            dp[i+k+1][j-k] = min(dp[i+k+1][j-k], dp[i][j] + abs(y2-y1) + abs(x2-x1))

# print(dp)
print(dp[-1][0])
