# 21608번 상어 초등학교
# https://www.acmicpc.net/problem/21608

"""
한 자리에 한 학생만 앉을 수 있고, 인접한 자리는 상하좌우
주어지는 다섯 개의 숫자는 (학생의 번호, 각 학생이 좋아하는 학생 4명)
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
   그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

"""
import sys
input = sys.stdin.readline


def search_expected_seats(friends):
    seats = [[0 for _ in range(N)] for _ in range(N)]
    friends_seats = []
    for friend in friends:
        if friend in d:
            friends_seats.append(d[friend])

    # 최대 수 찾기
    max_score = 0
    # 친구가 앉아 있다면
    if len(friends_seats):
        for y, x in friends_seats:
            for dy, dx in delta:
                ey = y + dy
                ex = x + dx
                if 0 <= ey < N and 0 <= ex < N:
                    if graph[ey][ex]:
                        continue
                    seats[ey][ex] += 1
                    max_score = max(max_score, seats[ey][ex])
        return seats, max_score

    # 친구가 앉아 있지 않다면
    for y in range(N):
        for x in range(N):
            # 이미 누가 앉았다면 패스
            if graph[y][x]:
                continue
            for dy, dx in delta:
                ey = y + dy
                ex = x + dx
                if 0 <= ey < N and 0 <= ex < N:
                    if graph[ey][ex]:
                        continue
                    seats[ey][ex] += 1
                    max_score = max(max_score, seats[ey][ex])
    return seats, max_score


def find_suitable_seat(number, seats, s):
    # print("seats", seats)
    second_seats = []
    for y in range(N):
        for x in range(N):
            if graph[y][x]:
                continue
            if seats[y][x] == s:
                second_seats.append((y, x))

    expected_score = 0
    expected_seat = second_seats[0]
    if len(second_seats) > 1:
        for y, x in second_seats:
            cnt = 0
            for dy, dx in delta:
                ey = y + dy
                ex = x + dx
                if 0 <= ey < N and 0 <= ex < N:
                    if graph[ey][ex]:
                        continue
                    cnt += 1
            if expected_score < cnt:
                expected_score = cnt
                expected_seat = (y, x)
        y, x = expected_seat
        graph[y][x] = number
        d[number] = (y, x)

    else:
        y, x = second_seats[0]
        graph[y][x] = number
        d[number] = (y, x)


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
d = dict()
students = dict()
for _ in range(N**2):
    arr = list(map(int, input().split()))
    num = arr[0]
    friends = arr[1:]
    students[num] = set(friends)
    expected_seats, score = search_expected_seats(friends)
    find_suitable_seat(num, expected_seats, score)
    # print(graph)

result = 0
for y in range(N):
    for x in range(N):
        target = graph[y][x]
        cnt = 0
        for dy, dx in delta:
            ey = y + dy
            ex = x + dx
            if 0 <= ey < N and 0 <= ex < N:
                if graph[ey][ex] in students[target]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)
