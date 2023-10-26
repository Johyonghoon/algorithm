# 2011번 암호코드
# https://www.acmicpc.net/problem/2011

"""
(1, 1)
(1, 0)
(1, 1)
(1, 1)

1 1 1 1 1
1 1 2 0 1
1 1 1 2 0
2 0 1 1 1
2 0 1 2 0
2 0 2 0 1

2가지 갈래가 가능할 때가 연속으로 존재할 경우 연속하는 개수에 따라
1, 2, 3, 5, 8 ... 로 증가한다.
즉, 피보나치를 적용

풀이 후 다른 풀이를 보니 너무 아름답다
DP 방향을 알면서도 이런 방식의 풀이만을 끌어낸 것이 아쉽다
잊을 만할 때쯤 다시 풀어봐야겠다.
"""

secrets = list(input())
N = len(secrets)
fibo = [0 for _ in range(5001)]
fibo[0] = 1
fibo[1] = 2
dp = []

for i in range(2, 5001):
    fibo[i] = fibo[i-1] + fibo[i-2]

for idx in range(N-1):
    cnt = 0
    # 0이 암호로 나온다면 한자리 수 0이나 0으로 시작하는 수는 암호가 안되므로 패스
    if secrets[idx] == '0':
        dp.append(0)
        continue
    if idx+1 < N and secrets[idx+1] != '0':
        cnt += 1
    if 0 < int(secrets[idx]+secrets[idx+1]) <= 26:
        if idx+2 < N and secrets[idx+2] == '0':
            dp.append(cnt)
            continue
        cnt += 2

    dp.append(cnt)

# print("dp", dp)

if secrets == ["0"]:
    isPossible = False
else:
    isPossible = True
result = 1
j = 0
cnt = 0

while j < N-1:
    if dp[j] == 3:
        cnt += 1
        j += 1

    elif dp[j] == 2:
        result *= fibo[cnt]
        result %= 1_000_000
        cnt = 0
        j += 2

    elif dp[j] == 1:
        result *= fibo[cnt]
        result %= 1_000_000
        cnt = 0
        j += 1

    else:
        isPossible = False
        break
    # print(j, cnt, result)

if cnt:
    result *= fibo[cnt]

if not isPossible:
    print(0)
else:
    print(result % 1_000_000)
