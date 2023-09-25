# 2885번 초콜릿 식사
# https://www.acmicpc.net/problem/2885

"""
# 정수론
풀고 보니 2진수로 변환하여
1이 나오는 첫 인덱스와 마지막 인덱스의 차이를 구하는 문제

1 : 1   => 0 - 0 = 0        1번 (1일 경우는 2부터 시작하므로 1번 쪼개고 시작)
4 : 100 => 0 - 0 = 0        0번 (단 0일 경우는 2의 배수이므로 0)
5 : 101 => 2 - 0 = 2 + 1,   3번
6 : 110 => 2 - 1 = 1 + 1,   2번
"""

K = int(input())
result = []
while K:
    result.append(K % 2)
    K //= 2

if len(result) == 1:
    print(2, 1)
else:
    s = result.index(1)
    result.reverse()
    e = len(result)-1 - result.index(1)
    if s == e:
        print(2 ** (len(result)-1), 0)
    else:
        print(2 ** len(result), e - s + 1)



"""
# 그리디 풀이
K = int(input())

chocolate = K
sqrt_cnt = 0

isSqrt = True
if K == 1:
    isSqrt = False

while K > 1:
    if K % 2:
        isSqrt = False
    sqrt_cnt += 1
    K //= 2

# print(isSqrt, sqrt_cnt, K)
if not isSqrt and K:
    sqrt_cnt += 1

cnt = 0
idx = sqrt_cnt
isDone = False
while chocolate:
    if chocolate == 2 ** idx:
        break
    elif chocolate > 2 ** idx:
        cnt += 1
        chocolate -= 2 ** idx
    else:
        cnt += 1
    idx -= 1

    # print(cnt, idx, isDone)


# 초콜릿의 개수는 K보다 큰 수 중 가장 작은 2의 제곱수
print(2**sqrt_cnt, cnt)
"""

