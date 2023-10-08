# 2174번 로봇 시뮬래아션
# https://www.acmicpc.net/problem/2174

"""
그래프 탐색은 상하반전을 했을 때 더 생각하기 쉽기 때문에 그런 관점으로 문제를 풀어보자
문제는 구현 그 자체인 것 같다.

명령의 종류
1. L : 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전
  - N -> W / W -> S / S -> E / E -> N
2. R : 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전
  - N -> E / E -> S -> S -> W / W -> zn
3. F : 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
  - N : y += 1
  - S : y -= 1
  - W : x -= 1
  - E : x += 1
"""

import sys
input = sys.stdin.readline

# A, B : 가로, 세로 땅의 크기
A, B = map(int, input().split())
graph = [[0 for _ in range(A)] for _ in range(B)]
# 로봇 초기 위치 및 방향
N, M = map(int, input().split())
robots = [[0, 0, "0"]]
for idx in range(N):
    a, b, d = input().split()
    x = int(a)
    y = int(b)
    robots.append([y-1, x-1, d])
    graph[y-1][x-1] = idx+1

# print(graph)

# 명령 시작
breaky = False
result = "OK"
for _ in range(M):
    num_str, command, cnt_str = input().split()
    num = int(num_str)
    cnt = int(cnt_str)

    for _ in range(cnt):
        if breaky:
            break

        # robots[num][0] : y축 좌표
        # robots[num][1] : x축 좌표
        # robots[num][2] : 로봇 방향

        if command == "L":
            if robots[num][2] == "N":
                robots[num][2] = "W"
            elif robots[num][2] == "W":
                robots[num][2] = "S"
            elif robots[num][2] == "S":
                robots[num][2] = "E"
            elif robots[num][2] == "E":
                robots[num][2] = "N"

        elif command == "R":
            if robots[num][2] == "N":
                robots[num][2] = "E"
            elif robots[num][2] == "E":
                robots[num][2] = "S"
            elif robots[num][2] == "S":
                robots[num][2] = "W"
            elif robots[num][2] == "W":
                robots[num][2] = "N"

        elif command == "F":
            # 방향이 북쪽
            if robots[num][2] == "N":
                # 바깥으로 벗어 난다면
                if robots[num][0] + 1 >= B:
                    result = f"Robot {num} crashes into the wall"
                    breaky = True
                    break
                elif graph[robots[num][0] + 1][robots[num][1]]:
                    result = f"Robot {num} crashes into robot {graph[robots[num][0] + 1][robots[num][1]]}"
                    breaky = True
                    break
                else:
                    graph[robots[num][0]][robots[num][1]] = 0
                    graph[robots[num][0] + 1][robots[num][1]] = num
                    robots[num][0] += 1
            # 방향이 동쪽
            elif robots[num][2] == "E":
                # 바깥으로 벗어 난다면
                if robots[num][1] + 1 >= A:
                    result = f"Robot {num} crashes into the wall"
                    breaky = True
                    break
                elif graph[robots[num][0]][robots[num][1]+1]:
                    result = f"Robot {num} crashes into robot {graph[robots[num][0]][robots[num][1]+1]}"
                    breaky = True
                    break
                else:
                    graph[robots[num][0]][robots[num][1]] = 0
                    graph[robots[num][0]][robots[num][1]+1] = num
                    robots[num][1] += 1

            # 방향이 남쪽
            elif robots[num][2] == "S":
                # 바깥으로 벗어 난다면
                if robots[num][0] - 1 < 0:
                    result = f"Robot {num} crashes into the wall"
                    breaky = True
                    break
                elif graph[robots[num][0]-1][robots[num][1]]:
                    result = f"Robot {num} crashes into robot {graph[robots[num][0]-1][robots[num][1]]}"
                    breaky = True
                    break
                else:
                    graph[robots[num][0]][robots[num][1]] = 0
                    graph[robots[num][0]-1][robots[num][1]] = num
                    robots[num][0] -= 1

            # 방향이 서쪽
            elif robots[num][2] == "W":
                # 바깥으로 벗어 난다면
                if robots[num][1] - 1 < 0:
                    result = f"Robot {num} crashes into the wall"
                    breaky = True
                    break
                elif graph[robots[num][0]][robots[num][1]-1]:
                    result = f"Robot {num} crashes into robot {graph[robots[num][0]][robots[num][1]-1]}"
                    breaky = True
                    break
                else:
                    graph[robots[num][0]][robots[num][1]] = 0
                    graph[robots[num][0]][robots[num][1]-1] = num
                    robots[num][1] -= 1
        # print(graph)

print(result)
