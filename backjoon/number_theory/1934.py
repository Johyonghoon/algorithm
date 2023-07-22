# 1934번 최소공배수
# https://www.acmicpc.net/problem/1934

# 최소공배수 : LCM(Least Common Multiple)
# 최대공약수 : GCF(Greatest Common Factor)

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m == 0:
        return n
    else:
        return gcd(n, m%n)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    G = gcd(A, B)
    print(A * B // G)


"""
# 왜 틀렸을까?

def prime_num(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print_numbers = []
for i in range(2, int(45000**(1/2))+1):
    if prime_num(i):
        print_numbers.append(i)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    gongbaesu = 1
    if A % B == 0:
        print(A)
        continue
    if B % A == 0:
        print(B)
        continue
    for i in print_numbers:
        
        while A % i == 0 or B % i == 0:
            if A % i == 0 and B % i == 0:
                A = A // i
                B = B // i
                gongbaesu *= i
                continue
            if A % i == 0:
                A = A // i
                gongbaesu *= i
                continue
            else:
                B = B // i
                gongbaesu *= i
                continue
        if A == 1 and B == 1:
            break
    print(gongbaesu)
"""