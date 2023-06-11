# 1912번 연속합
# https://www.acmicpc.net/problem/1912

n = int(input())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]

for i in range(n):
    prefix[i+1] = max(arr[i] + prefix[i], arr[i])

prefix.remove(0)
print(max(prefix))
