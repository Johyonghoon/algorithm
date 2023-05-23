# 17202 핸드폰 번호 궁합
# https://www.acmicpc.net/problem/17202
# import sys
#
# input = sys.stdin.readline

array_a = list(map(int, str(input())))
array_b = list(map(int, str(input())))
array_x = []

for i in range(8):
    array_x.append(array_a[i])
    array_x.append(array_b[i])

for i in range(15, 1, -1):
    for j in range(i):
        array_x[j] = (array_x[j] + array_x[j+1]) % 10

print(f"{array_x[0]}{array_x[1]}")
