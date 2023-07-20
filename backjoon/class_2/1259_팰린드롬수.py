# 1259번 팰린드롬수
# https://www.acmicpc.net/problem/1259

while True:
    x = input()
    if x == "0":
        break
    elif x == x[::-1]:
        print("yes")
    else:
        print("no")
