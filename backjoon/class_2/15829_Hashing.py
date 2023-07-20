# 15829번 Hashing
# https://www.acmicpc.net/problem/15829
r, M = 31, 1234567891
L = int(input())
arr = input()
hash_data = 0

for i in range(L):
    hash_data += (ord(arr[i]) - 96) * (r ** i)


if L < 8:
    print(hash_data)
else:
    print(hash_data // M)
