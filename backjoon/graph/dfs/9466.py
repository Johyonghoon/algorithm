# 9466번 텀 프로젝트
# https://www.acmicpc.net/problem/9466

"""
학생들이 S1, S2, ... Sr 이라고 할 때
r=1 이고 S1 -> S2 -> S3 ... -> Sr -> S1 을 선택하는 경우,
즉 루프가 발생하는 경우에만 한 팀이 될 수 있다.
그 결과로 팀에 속하지 않는 학생도 존재하게 된다.
주어진 선택 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(prnt, node, arr, cnt):
    global result
    if visited[node]:

        # 현재 탐색하고 있는 부모들의 자식들이라면
        if visited[node] == prnt:
            result -= cnt - arr.index(node)
            return

        # 만약 루프 생성 없이 다른 루프에서 탐색한 노드에 방문한 경우 종료
        else:
            return

    visited[node] = prnt
    nxt = students[node]
    arr.append(node)
    dfs(prnt, nxt, arr, cnt+1)


T = int(input())
for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(N+1)]
    result = N

    for idx in range(1, N+1):
        if visited[idx]:
            continue
        dfs(idx, idx, [], 0)

    print(result)
