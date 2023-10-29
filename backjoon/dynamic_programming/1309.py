# 1309번 동물원
# https://www.acmicpc.net/problem/1309

"""
N = 1
(0, 0) (1, 0) (0, 1)

N = 2
0 0  0 0  0 0  1 0  1 0  0 1  0 1
0 0  1 0  0 1  0 0  0 1  0 0  1 0
(0, 0) 3개 (1, 0) 2개 (0, 1) 2개 생김

(0, 0)일 경우 다음은 +3
(1, 0)일 경우 다음은 +2
(0, 1)일 경우 다음은 +2

N = 3

...
내 풀이는 틀린 풀이
근데 어디서 오류가 발생하는걸까

dp1 = [0 for _ in range(N+1)]
dp2 = [0 for _ in range(N+1)]
dp1[1] = 1
dp2[1] = 2

for idx in range(2, N+1):
    dp1[idx] = dp1[idx-1] * 3 % 9901
    dp2[idx] = dp2[idx-1] * 2 % 9901

print(dp1[N] + dp2[N])
"""

N = int(input())

if N == 1:
    print(3)
else:
    dp = [0 for _ in range(N+1)]
    dp[1] = 3
    dp[2] = 7
    for idx in range(3, N+1):
        dp[idx] = (dp[idx-1] * 2 + dp[idx-2]) % 9901

    print(dp[N])
