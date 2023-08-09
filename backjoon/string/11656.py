# 11656번 접미사 배열
# https://www.acmicpc.net/problem/11656

S = input()
arr = []

for i in range(len(S)):
    arr.append(S[i:len(S)])

arr.sort()
[print(i) for i in arr]
