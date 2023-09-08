# 2512번 예산
# https://www.acmicpc.net/problem/2512

"""
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여,
   그 이상인 예산요청에는 모두 상한액을 배정하고, 상한액 이하의 예산 요청에 대해서는 요청한 금액 배정
    ex) 전체 국가예산 485, [120, 110, 140, 150] 상한액 127 기준 [120, 110, 127, 127]
"""

N = int(input())
arr = list(map(int, input()))
budget = int(input())

total = sum(arr)
# 전체의 합이 예산 안이라면 바로 최대값 출력
if total <= budget:
    print(max(arr))

# 아니라면, 상한액 찾기
else:
    maxi = budget // N



