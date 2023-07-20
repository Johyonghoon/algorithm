t = int(input())

while t != 0:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    d = []
    index = 0
    for i in range(n):
        d.append(arr[index: index+m])
        index += m
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] += max(d[i][j-1], d[i+1][j-1])
            elif i == n-1:
                d[i][j] += max(d[i][j-1], d[i-1][j-1])
            else:
                d[i][j] += max(d[i][j-1], d[i+1][j-1], d[i-1][j-1])
    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    print(result)
    t -= 1
