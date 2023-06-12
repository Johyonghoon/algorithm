# 2247번 실질적 약수
# https://www.acmicpc.net/problem/2247

n = int(input())
result = 0
for i in range(2, n//2+1):
    result += ((n // i) - 1) * i
    result %= int(1e6)
print(result)

"""


99 3 9 11 33
100 2 5 10 20 50

"""