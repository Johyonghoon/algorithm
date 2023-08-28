# 14889번 스타트와 링크
# https://www.acmicpc.net/problem/14889

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def calc_stats(arr):
    total = 0
    for i in arr:
        for j in arr:
            if i == j:
                continue
            total += graph[i][j]
    return total


def team(node, start_team):
    # 한 팀이 구성되었을 때 반대 팀은 남은 인원으로 구성됨
    if len(start_team) == N//2:
        link_team = []
        for person in people:
            if person in start_team:
                continue
            link_team.append(person)
        result.append(abs(calc_stats(start_team) - calc_stats(link_team)))
        # print(start_team)
        return

    # 가장 마지막에 포함된 노드를 기준으로 더 큰 번호의 사람들만 탐색(중복 방지)
    for nxt in range(node+1, N):
        start_team.append(nxt)
        team(nxt, start_team)
        start_team.pop()


N = int(input())
# 팀 나누기
people = [i for i in range(N)]

# 능력치 정보
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = []
team(0, [])

result.sort()
print(result[0])


"""
20
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 0 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 0 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 0 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 0 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 0 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 0 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 0 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 0 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 0 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 0 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 0 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 0 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 0 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 0 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 0
"""