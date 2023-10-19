# 17951번 흩날리는 시험지 속에서 내 평점이 느껴진거야
# https://www.acmicpc.net/problem/17951

"""
# 이분탐색 - 파라메트릭 서치
K개의 그룹으로 나눈 후 각 그룹에서 맞은 문제 개수의 합 중 최솟값의 최대 점수를 구하는 문제
"""


def parametric_search():
    global result
    start = 1
    end = sum(scores)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        total = 0
        for idx in range(N):
            total += scores[idx]
            if total >= mid:
                cnt += 1
                total = 0

        # 구간 합을 충족할 때 탐색값 키우기
        if cnt >= K:
            result = max(result, mid)
            start = mid + 1
        # 구간 합을 충족하는 개수가 적을 때 탐색값 줄이기
        else:
            end = mid - 1


N, K = map(int, input().split())
scores = list(map(int, input().split()))

result = 0
parametric_search()
print(result)
