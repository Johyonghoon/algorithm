# 8320번 직사각형을 만드는 방법
# https://www.acmicpc.net/problem/8320

"""
1을 포함한 약수를 구하는 문제
"""


n = int(input())

cnt = 0
for idx in range(1, n+1):
    for j in range(1, int(idx**(1/2))+1):
        if idx % j == 0:
            cnt += 1

print(cnt)
