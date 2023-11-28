# 16922번 로마 숫자 만들기
# https://www.acmicpc.net/problem/16922

"""
이걸 백트래킹 어떻게 하지...
"""
import sys
sys.setrecursionlimit(10**8)

N = int(input())
seti = set()
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = N-i-j-k
            seti.add(i + 5*j + 10*k + 50*l)

print(len(seti))
