# 17626번 Four Squares
# https://www.acmicpc.net/problem/17626

import sys
sys.setrecursionlimit(10**9)


def recur(node, total, cnt):
    global result

    # 목표에 도달했다면 결과 업데이트
    if total == N:
        # print("result", node, total, cnt)
        result = min(result, cnt)
        return

    # 이미 최소 개수에 도달했다면 패스
    if cnt + 1 >= result:
        return

    for nxt in range(node, -1, -1):
        # 다음 값이 목표값을 넘어섰다면 넘어가기
        if total + sqrs[nxt] > N:
            continue
        recur(nxt, total+sqrs[nxt], cnt+1)


N = int(input())
# 제곱수를 모두 구하기
sqrs = []
for idx in range(1, int(N**(1/2))+1):
    sqrs.append(idx**2)

# 넷 이하의 제곱수의 합으로 표현할 수 있다고 이미 증명했으므로 최대는 4
result = 4
recur(len(sqrs)-1, 0, 0)
print(result)
