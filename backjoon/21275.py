# 21275번 폰 호석만
# https://www.acmicpc.net/problem/21275

alpabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]
jinbub = list(range(10)) + alpabet
breaky = False
result = []

A, B = input().split()

if A == B:
    for idx in A:
        result += [0, 0]
        if idx in alpabet:
            result = []
            break
    breaky = True
A = list(str(A))
B = list(str(B))

dpa = [0 for _ in range(37)]
dpb = [0 for _ in range(37)]

for idx in A:
    if idx not in jinbub:
        breaky = True
        break

for idx in B:
    if idx not in jinbub:
        breaky = True
        break

if breaky:
    pass
else:

    for idx in range(jinbub.index(max(A))+1, 37):
        k = 0
        for j in A[::-1]:
            dpa[idx] += jinbub.index(j) * (idx ** k)
            k += 1

    for idx in range(jinbub.index(max(B))+1, 37):
        k = 0
        for j in B[::-1]:
            dpb[idx] += jinbub.index(j) * (idx ** k)
            k += 1

    for a, ax in enumerate(dpa):
        if ax == 0:
            continue
        for b, bx in enumerate(dpb):
            if bx == 0:
                continue
            if ax == bx:
                if a == b:
                    continue
                result.append((ax, a, b))

if len(result) > 1:
    print("Multiple")
elif len(result) == 1:
    print(*result[0])
else:
    print("Impossible")
