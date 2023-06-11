# 14232번 보석 도둑
# https://www.acmicpc.net/problem/14232

k = int(input())
arr = []
for i in range(2, int(k **(1/2))+1):
    while k % i == 0:
        arr.append(i)
        k = k // i

if k > k**(1/2)+1:
    arr.append(k)

print(len(arr))
print(*arr)
