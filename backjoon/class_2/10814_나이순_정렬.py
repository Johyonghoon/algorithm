# 10814번 나이순 정렬
# https://www.acmicpc.net/problem/10814

N = int(input())
arr = []
for idx in range(N):
    age, name = input().split()
    arr.append([int(age), idx, name])

arr.sort()
[print(i[0], i[2]) for i in arr]

