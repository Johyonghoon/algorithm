# 11052번 카드 구매하기
# https://www.acmicpc.net/problem/11052

N = int(input())
prices = [0] + list(map(int, input().split()))
for i in range(2, N+1):
    for j in range(i//2, i):
        prices[i] = max(prices[i], prices[j] + prices[i-j])

print(prices[N])
