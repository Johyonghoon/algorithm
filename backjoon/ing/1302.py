# 1302번 베스트셀러
# https://www.acmicpc.net/problem/1302
import sys
input = sys.stdin.readline

# 책이 입력될 때, 개수를 증가
d = {}
# 최대 개수를 미리 파악
maxi = 0

# 책 정보 입력
N = int(input())
for _ in range(N):
    book = input().rstrip()
    if book not in d:
        d[book] = 1
    else:
        d[book] += 1

    if maxi < d[book]:
        maxi = d[book]

# 딕셔너리 key value 값을 순회하며, 개수가 maximum 인 것을 찾고,
# 여러 개일 때는, 비교해서 사전 순으로 앞서는 책의 이름을 result 에 저장
result = ""
for k, v in d.items():
    if v == maxi:
        if result:
            if result > k:
                result = k
        else:
            result = k

print(result)
