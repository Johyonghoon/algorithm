# 15649번 N과 M 1
# https://www.acmicpc.net/problem/15649


def recur():
    global arr

    # 만약 만족하는 길이에 도달했다면 출력
    if len(arr) == M:
        print(*arr)
        return

    # 사전 순으로 증가하므로 1부터 탐색하여 깊이우선탐색
    for nxt in range(1, N+1):
        # 만약 이미 수열에 포함되어 있다면 패스
        if nxt in arr:
            continue
        # 수열에 포함
        arr.append(nxt)
        recur()
        # 가지치기가 끝났다면 수열에서 빼주기
        arr.pop()


N, M = map(int, input().split())
arr = []
recur()
