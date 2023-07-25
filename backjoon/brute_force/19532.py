# 19532번 수학은 비대면강의입니다
# https://www.acmicpc.net/problem/19532

A, B, C, D, E, F = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if A * x + B * y == C:
            if D * x + E * y == F:
                print(x, y)
                break


"""
a, b, c, d, e, f = map(int, input().split())
print((c * e - b * f) // (a * e - b * d), (c * d - a * f) // (b * d - a * e))

y = (cd - af) / (bd - ae)
x = (ce - bf) / (ae - bd)
"""