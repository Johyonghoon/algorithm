every = set()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 666]
for i in arr:
    for j in arr:
        for k in arr:
            for l in arr:
                for m in arr:
                    num = str(i) + str(j) + str(k) + str(l) + str(m)
                    if "666" in num:
                        every.add(int(num))

every = sorted(list(every))

N = int(input())
print(every[N-1])

"""
0666
1666
...
5666
6660
6661
...
6669
9666
10666
"""