# # 15489번 파스칼 삼각형
# # https://www.acmicpc.net/problem/15489
#
# R, C, W = map(int, input().split())
# dp = [[0 for _ in range(31)] for _ in range(31)]
# # print(R, C, W)
#
# # 파스칼 삼각형 만들기
# for i in range(1, 31):
#     dp[i][1] = 1
#     dp[i][i] = 1
#     for j in range(1, i):
#         dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#
# # for i in dp:
# #     print(i)
#
# result = 0
# for i in range(W):
#     for j in range(i+1):
#         # print(R+i, C+j, dp[R+i][C+j])
#         result += dp[R+i][C+j]
#
# print(result)
#

# ------------ 틀린 것 (원인 파악중) ----------------
# 15489번 파스칼 삼각형
# https://www.acmicpc.net/problem/15489

R, C, W = map(int, input().split())
dp = [[0 for _ in range(32)] for _ in range(32)]
# print(R, C, W)

# 파스칼 삼각형 만들기
for i in range(1, 32):
    dp[i][1] = 1
    for j in range(2, 32):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for i in dp:
    print(i)

result = 0
for i in range(R, R+W):
    for j in range(C, C+W+R-i):
        # print(i, j, dp[i][j])
        result += dp[i][j]

print(result)
