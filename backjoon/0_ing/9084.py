# 9084 동전
# 동전의 개수가 아닌, 금액을 만드는 모든 방법의 횟수
"""
1 2
m=1
(1, 0)
m=2
(2, 0)
(0, 1)
m=3
(3, 0)
(1, 1)
m=4
(4, 0)
(2, 1)
(0, 2)
m=5
(5, 0)
(3, 1)
(1, 2)

1 5 10
m=1
(1, 0, 0)
m=2
(2, 0, 0)
...
m=5
(5, 0, 0)
(0, 1, 0)
m=6
(6, 0, 0)
(1, 1, 0)
"""

T = int(input())
for _ in range(T):
    N = int(input())
    DP = [0 for _ in range(10001)]
    coins = list(map(int, input().split()))
    for coin in coins:
        DP[coin] = 1

    M = int(input())

    for i in range(2, M+1):

        for coin in coins[::-1]:
            if coin > i:
                continue
            if i % coin > 0:
                continue
            DP[i] += DP[i - coin] + 1
            break

    print(DP[:20])
    print(DP[M])
