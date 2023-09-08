# 2597번 줄자접기
# https://www.acmicpc.net/problem/2597


L = int(input())
ruler = [0 for _ in range(L+1)]

red = sorted(list(map(int, input().split())))
blue = sorted(list(map(int, input().split())))
yellow = sorted(list(map(int, input().split())))

# 줄자의 길이 초기화
start = 0
end = L

# red : 중간 지점을 기준으로 짧은 길이를 빼기
if red[0] != red[1]:
    # 접히는 좌표 찾기
    r_middle = sum(red) / 2

    # 짧은 길이의 좌표를 반대로 넘겨주기
    if r_middle - start <= end - r_middle:
        # 길이 업데이트
        L -= r_middle - start
        # 시작점 업데이트
        start = r_middle
        # 접히는 지점보다 좌표가 작을 때
        for idx in range(2):
            if blue[idx] < start:
                blue[idx] = int(start + start - blue[idx])
            if yellow[idx] < start:
                yellow[idx] = int(start + start - yellow[idx])

    else:
        L -= end - r_middle
        end = r_middle
        # 접히는 지점보다 좌표가 클 때
        for idx in range(2):
            if blue[idx] > end:
                blue[idx] = int(end - (blue[idx] - end))
            if yellow[idx] > end:
                yellow[idx] = int(end - (yellow[idx] - end))

    # 다시 좌표 정렬
    blue.sort()
    yellow.sort()

# print(L)
# print(blue)
# print(yellow)

# blue : 중간 지점을 기준으로 짧은 길이를 빼기
if blue[0] != blue[1]:
    # 접히는 좌표 찾기
    b_middle = sum(blue) / 2

    # 짧은 길이의 좌표를 반대로 넘겨주기
    if b_middle - start <= end - b_middle:
        # 길이 업데이트
        L -= b_middle - start
        # 시작점 업데이트
        start = b_middle
        # 접히는 지점보다 좌표가 작을 때
        for idx in range(2):
            if yellow[idx] < start:
                yellow[idx] = int(start + start - yellow[idx])

    else:
        L -= end - b_middle
        end = b_middle
        # 접히는 지점보다 좌표가 클 때
        for idx in range(2):
            if yellow[idx] > end:
                yellow[idx] = int(end - (yellow[idx] - end))

    # 다시 좌표 정렬
    yellow.sort()

# yellow : 중간 지점을 기준으로 짧은 길이를 빼기
if yellow[0] != yellow[1]:
    # 접히는 좌표 찾기
    y_middle = sum(yellow) / 2

    # 짧은 길이의 좌표를 반대로 넘겨주기
    if y_middle - start <= end - y_middle:
        # 길이 업데이트
        L -= y_middle - start

    else:
        L -= end - y_middle

print(f"{L:.1f}")




"""
10
2 7
5 4
10 3
ans : 3.5

100
25 75
40 60
10 90

ans : 50.0

100
25 75
30 90
40 75
# start : 50, end : 100
# start : 50, end : 80
# start : 50, end : 67.5
ans : 17.5

5
0 5
3 5
2 4
ans : 1.0

77
45 60
23 54
31 70
ANS : 33.0
"""
