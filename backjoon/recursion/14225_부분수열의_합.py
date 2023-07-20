# 14225번 부분수열의 합
# https://www.acmicpc.net/problem/14225

N = int(input())
arr = list(map(int, input().split()))
seti = set()

def recur(idx, number):
    if idx == N:
        seti.add(number)
        return

    recur(idx+1, number)
    recur(idx+1, number+arr[idx])

recur(0, 0)

for i in range(1, int(1e9)):
    if i in seti:
        continue
    print(i)
    break
