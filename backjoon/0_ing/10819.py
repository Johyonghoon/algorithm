# 10819번 차이를 최대로
# https://www.acmicpc.net/problem/10819


def recur(arr):
    global result
    # print(arr)
    # N 길이의 배열을 생성했을 때 차이의 합을 저장
    if len(arr) == N:
        total = 0
        for idx in range(len(arr)-1):
            total += abs(arr[idx] - arr[idx+1])
        result = max(result, total)
        return

    # 인덱스 탐색하며 모든 순서의 배열을 생성
    for nxt in range(N):
        if visited[nxt]:
            continue
        visited[nxt] = 1
        arr.append(A[nxt])
        recur(arr)
        arr.pop()
        visited[nxt] = 0


N = int(input())
A = list(map(int, input().split()))

visited = [0 for _ in range(N)]
result = 0
recur([])

print(result)
