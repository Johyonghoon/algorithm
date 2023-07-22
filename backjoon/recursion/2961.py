# 2961번 도영이가 만든 맛있는 음식
# https://www.acmicpc.net/problem/2961

N = int(input())
arr = []
result = []
for _ in range(N):
    sin, son = map(int, input().split())
    arr.append([sin, son])

def recur(idx, sin, son):
    if idx == N:
        if sin == 1 and son == 0:
            return
        result.append(abs(sin-son))
        return
    recur(idx+1, sin, son)
    recur(idx+1, sin * arr[idx][0], son + arr[idx][1])

recur(0, 1, 0)
print(min(result))
