# 2309번 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

arr = []
for _ in range(9):
    arr.append(int(input()))
result = []

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            del arr[j]
            del arr[i]
            break
    if len(arr) == 7:
        break

arr.sort()
[print(i) for i in arr]
