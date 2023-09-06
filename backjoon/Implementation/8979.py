# 8979번 올림픽
# https://www.acmicpc.net/problem/8979

"""
국가간 순위
1. 금메달 수가 더 많은 나라
2. 금메달 수가 같다면 은메달 수가 더 많은 나라
3. 금 은메달 수가 같으면 동메달 수가 더 많은 나라
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    nation, G, S, B = map(int, input().split())
    arr.append([G, S, B, nation])

# 등수 정보 파악을 위한 내림차순 정렬
arr.sort(reverse=True)

# 국가 등수 정보를 입력할 배열 초기화
ranks = [0 for _ in range(N)]

# 반복문 탐색을 위한 변수
rank = 0
idx = 0
pre = []
cnt = 0

# 모든 국가를 탐색할 때
while idx < N:
    # 만약 메달 수가 모두 같지 않다면 등수는 늘어난다.
    if pre != arr[idx][:3]:
        rank += 1 + cnt
        cnt = 0
    # 메달 수가 같다면 공동 등수가 생겨 다음 국가의 둥수가 미뤄지므로 카운트하여 계산
    else:
        cnt += 1
    # 국가 번호
    n = arr[idx][-1]

    # 인덱스에 맞게 삽입
    ranks[n-1] = rank
    # 이전의 메달 정보 입력
    pre = arr[idx][:3]
    idx += 1

print(ranks[K-1])




