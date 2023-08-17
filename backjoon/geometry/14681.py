# 14681번 사분면 고르기
# https://www.acmicpc.net/problem/14681

x = int(input())
y = int(input())

# 문제조건) x != 0 and y != 0
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
