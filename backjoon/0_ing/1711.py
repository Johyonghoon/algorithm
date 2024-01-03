# 1711번 직각삼각형
# https://www.acmicpc.net/problem/1711

import sys
input = sys.stdin.readline


def solve(N, coor):
    global result

    for i in range(N):
        ay, ax = coor[i]
        for j in range(i+1, N):
            by, bx = coor[j]
            len1 = (ay - by) ** 2 + (ax - bx) ** 2
            for k in range(j+1, N):
                cy, cx = coor[k]
                len2 = (by - cy) ** 2 + (bx - cx) ** 2
                len3 = (cy - ay) ** 2 + (cx - ax) ** 2
                if len1 + len2 + len3 == max(len1, len2, len3) * 2:
                    result += 1


if __name__ == '__main__':
    N = int(input())
    coordinate = []
    for _ in range(N):
        x, y = map(int, input().split())
        coordinate.append([y, x])
    result = 0
    solve(N, coordinate)
    print(result)
