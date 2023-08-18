# 11721번 열 개씩 끊어 출력하기
# https://www.acmicpc.net/problem/11721

s = input()
# idx 가 10이 되면 줄바꿈
idx = 0
for c in s:
    idx += 1
    print(c, end="")
    if idx == 10:
        print()
        idx = 0
