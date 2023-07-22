# 1075번 나누기
# https://www.acmicpc.net/problem/1075

N = int(input())
F = int(input())

num = N // 100 * 100
for i in range(100):
    number = num + i
    if number % F == 0:
        if i < 10:
            print(0, end="")
        print(i)
        break
