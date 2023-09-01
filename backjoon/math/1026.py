# 1026번 보물
# https://www.acmicpc.net/problem/1026

"""
한 배열의 큰 수와 다른 한 배열의 작은 수가 곱해지면 최소값이 되지 않을까?
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 한 배열은 오름차순, 다른 한 배열은 내림차순으로 정렬
A.sort()
B.sort(reverse=True)

# 곱하고 더하기
result = 0
for idx in range(N):
    result += A[idx] * B[idx]

# 결과 출력
print(result)