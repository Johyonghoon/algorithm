# 2527번 직사각형
# https://www.acmicpc.net/problem/2527

"""
(ax, aq)  (ap, aq)  (bx, bq)  (bp, bq)
(ax, ay)  (ap, ay)  (bx, by)  (bp, by)
"""


for _ in range(4):
    ax, ay, ap, aq, bx, by, bp, bq = map(int, input().split())

    # 절대 만날 수 없을 때
    if ap < bx or ax > bp or aq < by or ay > bq:
        print("d")
    # 각 꼭지점만이 마주할 때
    elif (ap == bx and aq == by) or (ap == bx and ay == bq) \
            or (ax == bp and aq == by) or (ax == bp and ay == bq):
        print("c")
    # 변이 맞닿을 때
    elif ((ax == bp or ap == bx) and (by <= ay < bq or by < aq <= bq)) \
            or ((bx == ap or bp == ax) and (ay <= by < aq or ay < bq <= aq)) \
            or ((ay == bq or aq == by) and (bx <= ax < bp or bx < ap <= bp)) \
            or ((by == aq or bq == ay) and (ax <= bx < ap or ax < bp <= ap)):
        print("b")
    # 공통 너비가 존재할 때
    else:
        print("a")



"""
9
8
7                   a   a   a   a
6                   a   a   a   a
5                   ba   a   a   a
4                   ba   a   a   a  
3                   ba   a   a   a
2                   ba   a   a   a
1   b   b   b   b   b
0           
"""