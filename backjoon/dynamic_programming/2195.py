# 2195번 문자열 복사
# https://www.acmicpc.net/problem/2195

"""
# 탑다운 dp
copy(3, 2)
=> S의 3번 문자부터 2개 문자를 P에 복사해서 붙인다는 의미
"""
import sys

sys.setrecursionlimit(10**9)


def recur(idx):
    # 끝에 도달했을 때에는 더이상 더할 것이 없다.
    if idx == M:
        dp[idx] = 0
        return 0
    if idx > M:
        return int(1e9)
    # 이미 저장한 값은 다시 계산하지 않는다.
    if dp[idx] != int(1e9):
        return dp[idx]

    # 남은 P의 길이만큼 탐색
    for j in range(1, M+1-idx):
        # 해당 길이의 문자에 해당하는 문자가 set에 존재하지 않는다면 종료
        if P[idx:idx+j] not in set_s:
            break
        # 탐색한 개수와 이미 탐색한 개수를 비교하여 최소값을 저장
        dp[idx] = min(recur(idx+j)+1, dp[idx])
    return dp[idx]


S = input()
N = len(S)
P = input()
M = len(P)

# 가능한 문자를 탐색
set_s = set()
for i in range(N+1):
    for j in range(i+1, N+1):
        set_s.add(S[i:j])

dp = [int(1e9) for _ in range(M+1)]
recur(0)
print(max(dp))

"""
input
abaabba
aaabbbabbbaaa
output
6

input
xy0z
zzz0yyy0xxx
output
10
"""
