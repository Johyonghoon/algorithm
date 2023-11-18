# 12018번 Yonsei TOTO
# https://www.acmicpc.net/problem/12018

"""
주어진 마일리지로 최대한 들을 수 있는 과목 개수
N개 과목에 대해 신청한 사람 수 P와 수강인원 L이 주어지고, 각 사람의 마일리지가 주어진다.
만약 4명이 수강할 수 있는 과목에 5명이 신청했다면, 하위 2등의 마일리지 만큼은 신청해야 한다.
하지만, 마일리지는 하나 과목에 1에서 36까지 넣을 수 있다.
따라서 넣지 않는 것은 되지 않는다.
만약 마일리지가 같다면 성준이에게 우선순위가 주어진다.
"""

N, M = map(int, input().split())
needs = []
for _ in range(N):
    P, L = map(int, input().split())
    mileages = list(map(int, input().split()))
    mileages.sort(reverse=True)
    if L <= P:
        # 혹시나 다른 사람은 마일리지를 더 많이 넣을 수 있을까봐...
        if mileages[L-1] > 36:
            continue
        needs.append(mileages[L-1])
    else:
        # 최소 1은 넣어야 함
        needs.append(1)

needs.sort()
# print(needs)
cnt = 0
for need in needs:
    if M >= need:
        cnt += 1
        M -= need
    else:
        break

print(cnt)
