# 10971번 외판원 순회 2
# https://www.acmicpc.net/problem/10971

"""
외판원 순회(Traveling Salesman Problem(TSP)
1~N번 번호의 도시를 모두 거쳐 다시 원래의 도시로 돌아올 때 가장 적은 비용을 들이는 방법
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(cnt, node, plan):
    global result
    if cnt == N:
        # 0이면 갈 수 없는거니까
        if cost[plan[-1]][plan[0]]:
            # 마지막 인덱스에서 처음 인덱스로 돌아오는 값도 더해줘야 한다
            total = 0
            for k in range(N):
                # k에서 k-1은 거꾸로다..
                # k-1에서 k로 이동하는 값을 더해야 함
                total += cost[plan[k-1]][plan[k]]
            # print(plan, total)
            result = min(result, total)
        return

    # 간선 정보를 만들어 두고 전체 범위를 탐색하는 바보 짓을 했다.
    # 그래서 시간초과 메모리 초과,, ㄴㄴ,, 그래도 시간초과
    # 무한의 굴레에 빠진 건가
    for nxt in edge[node]:
        if cost[node][nxt] == 0:    # 자기 자신을 포함하여 가지 못할 때
            continue
        if nxt in plan:
            continue

        plan.append(nxt)
        recur(cnt+1, nxt, plan)
        plan.pop()


N = int(input())
edge = [[] for _ in range(N)]
cost = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j, num in enumerate(arr):
        if num:
            edge[i].append(j)
    cost.append(arr)

result = 10**8
# 시작점을 정해두고 시작하자
# for idx in range(N):
# 0을 거쳐가는 순회가 존재한다면 다른 지점을 출발점을 두더라도 같은 방법을 이미 탐색하지 않을까
recur(1, 0, [0])

print(result)
