t = int(input())

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return factorial(x-1) * x

while t != 0:
    n, m = map(int, input().split())
    d = [factorial(i) for i in range(m+1)]
    print(d[m] // (d[n] * d[m-n]))
    t -= 1