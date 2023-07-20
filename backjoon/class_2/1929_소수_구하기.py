# 1929번 소수 구하기
# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())
arr = [True for _ in range(n+1)]

def prime_number(x):
    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if i == 1:
        continue
    if prime_number(i) is True:
        print(i)
