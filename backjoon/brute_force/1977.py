# 1977번 완전제곱수
# https://www.acmicpc.net/problem/1977

M = int(input())
N = int(input())

total = 0
small = int(1e9)
for num in range(M, N+1):
    if int(num**(1/2)) == num**(1/2):
        total += num
        small = min(small, num)

if total == 0:
    print(-1)
else:
    print(total)
    print(small)
