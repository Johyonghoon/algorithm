# 1788번 피보나치 수의 확장
# https://www.acmicpc.net/problem/1788

"""
피보나치 수
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1
fobo[3] = 2 ...

fibo[0] = 0
fibo[1] = fibo[0] + fibo[-1]
fibo[-1] = fibo[1] - fibo[0] = 1 - 0 = 1
fibo[-2] = fibo[0] - fibo[-1] = 0 - 1 = -1
fibo[] = [0, 1, -1, 2, -3, 5, -8, 13, -21, 34...]
N이 짝수이면 음수, 홀수이면 양수
"""
fibo = [0 for _ in range(1_000_001)]
fibo[1] = 1

for i in range(2, 1_000_001):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % int(1e9)
# print(fibo[:10])

N = int(input())
if N == 0:
    print(0)
    print(0)
elif N > 0:
    print(1)
    print(fibo[N])
else:
    if (-N) % 2:
        print(1)
    else:
        print(-1)
    print(fibo[-N])
