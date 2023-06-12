# 2609번 최대공약수와 최대공배수
# https://www.acmicpc.net/problem/2609
# Not solved

n, m = map(int, input().split())
small = 1
big = n * m
prime_factor_n = {}
prime_factor_m = {}

for i in range(2, int(n**(1/2))+1):
    while n % i == 0:
        if not i in prime_factor_n:
            prime_factor_n[i] = 0
        prime_factor_n[i] += 1
        n = n // i

if n > n**(1/2):
    if not n in prime_factor_n:
        prime_factor_n[n] = 1

for i in range(2, int(m**(1/2))+1):
    while m % i == 0:
        if not i in prime_factor_m:
            prime_factor_m[i] = 0
        prime_factor_m[i] += 1
        m = m // i

if m > m**(1/2):
    if not m in prime_factor_m:
        prime_factor_m[m] = 1

for key, value in prime_factor_n.items():
    small *= key ** (min(value, prime_factor_m[key]))

print(small)
print(big // small)
