# 1816번 암호 키
# https://www.acmicpc.net/problem/1816


def prime_number(x):
    for i in range(2, int(1e6)):
        if x % i == 0:
            return False
    return True


n = int(input())
for _ in range(n):
    x = int(input())
    if prime_number(x) is True:
        print("YES")
    else:
        print("NO")
