# 9020번 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

def prime_num(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

prime_numbers = []
for i in range(2, 10000):
    if prime_num(i):
        prime_numbers.append(i)

T = int(input())
for _ in range(T):
    a, b = 0, 10000
    N = int(input())
    start = N // 2
    while True:
        if not start in prime_numbers:
            start -= 1
        if start in prime_numbers:
            break
    for idx in prime_numbers[prime_numbers.index(start)::-1]:
        if idx > N // 2:
            break
        if N - idx in prime_numbers:
            a = idx
            b = N - idx
            print(a, b)
            break
