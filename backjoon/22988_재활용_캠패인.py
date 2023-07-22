# 22988번 재활용 캠패인
# https://www.acmicpc.net/problem/22988

N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))
start = 0
end = N-1
while start < end:
    if arr[end] == X:
        end -= 1
        continue
    if arr[start] + arr[end] + X/2 >= X:
        arr[end] = min(X, arr[start] + arr[end] + X/2)
        arr[start] = -1
        start += 1
        end -= 1
    else:
        start += 1

etc = []
for num in arr:
    if num != -1 and num != X:
        etc.append(num)

a = 0
if len(etc) > 0:
    a = int(sum(etc) + X/2 * (len(etc) - 1)) // X

print(int(arr.count(X) + a))

"""
7 13 => 6.5
0 1 2 3 5 8 13
"""