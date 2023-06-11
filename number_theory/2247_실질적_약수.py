# 2247번 실질적 약수
# https://www.acmicpc.net/problem/2247
import sys

n = int(sys.stdin.readline())
prime_number = []
result = 0

def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(2, int(n**(1/2))+1):
    if prime_number(i):
        result += i * (n // i - 1)

print(result % int(1e6))

"""


99 3 9 11 33
100 2 5 10 20 50

"""