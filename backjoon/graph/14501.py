# 14501번 퇴사
# https://www.acmicpc.net/problem/14501

N = int(input())
arr = []
result = []
for _ in range(N):
    date, price = map(int, input().split())
    arr.append([date, price])

def recur(idx, price):
    if idx == N:
        result.append(price)
        return
    elif idx > N:
        return
    recur(idx + arr[idx][0], price + arr[idx][1])
    recur(idx+1, price)

recur(0, 0)
print(max(result))
