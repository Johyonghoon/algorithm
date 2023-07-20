n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
d = [1 for _ in range(n)]

# LIS(Longest Icreasing Subsequence)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - d[n-1])
