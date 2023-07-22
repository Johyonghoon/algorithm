# 4948번 베르트랑 공준
# https://www.acmicpc.net/problem/4948

def prime_num(x):
    for idx in range(2, int(x**(1/2))+1):
        if x % idx == 0:
            return False
    return True

prime_numbers = []

for idx in range(2, 123456*2+1):
    if prime_num(idx):
        prime_numbers.append(idx)

while True:
    cnt = 0
    N = int(input())
    if N == 0:
        break
    for i in prime_numbers:
        if N < i <= 2*N:
            cnt += 1
    print(cnt)
