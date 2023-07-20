# 1978번 소수 찾기
# https://www.acmicpc.net/problem/1978

n = int(input())
arr = list(map(int, input().split()))
cnt = 0

def prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in arr:
    if prime_number(i) is True:
        cnt += 1

print(cnt)