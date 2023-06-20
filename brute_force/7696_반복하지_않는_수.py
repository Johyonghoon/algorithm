# 7696번 반복하지 않는 수
# https://www.acmicpc.net/problem/7696
# from collections import defaultdict
#
#
# dp = [0 for _ in range(1000001)]
#
# while True:
#
#     N = int(input())
#     if N == 0:
#         break
#
#     n = 0
#     cnt = 0
#     while True:
#
#         for i in range(1, N):
#
#             if dp[i] != 0:
#                 continue
#
#             for j in range(dp[i-1], int(1e9)):
#
#
#             if i > 10:
#                 breaky = False
#                 d = defaultdict(int)
#                 temp = str(n)
#                 for i in temp:
#                     if temp.count(i) > 1:
#                         breaky = True
#                         break
#                 if breaky:
#                     continue
#
#             cnt += 1
#             dp()
#         if cnt == N:
#             break
#     if cnt == N:
#         print(n)
#         continue
