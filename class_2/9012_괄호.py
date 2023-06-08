# 9012번 괄호
# https://www.acmicpc.net/problem/9012

T = int(input())
while T != 0:
    arr = input()
    x = 0
    for i in arr:
        if i == '(':
            x += 1
        else:
            x -= 1
            if x < 0:
                break
    if x == 0:
        print('YES')
    else:
        print('NO')
    T -= 1
