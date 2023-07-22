# 2581번 소수
# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

def prime_num(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

total = 0
mini = 10001


for i in range(M, N+1):
    if prime_num(i):
        total += i
        mini = min(mini, i)

if total == 0:
    print(-1)
else:
    print(total)
    print(mini)

