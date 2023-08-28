# 1417번 국회의원 선거
# https://www.acmicpc.net/problem/1417

import sys
input = sys.stdin.readline

N = int(input())
candidates = [0]
for idx in range(1, N+1):
    candidates.append(int(input()))

result = 0
# 1번 후보자의 득표수가 최대가 아닐 때
while candidates[1] != max(candidates):
    # 최다 득표자의 인덱스를 찾아 득표수를 차감하고 1번 후보자에게 추가
    sorted_candidates = sorted(candidates)
    maximum = sorted_candidates[-1]
    max_index = candidates.index(maximum)
    candidates[max_index] -= 1
    candidates[1] += 1
    result += 1

# 만약 최대 득표자가 한 명 이상 더 있다면, 한 표를 더 매수
if candidates.count(candidates[1]) != 1:
    result += 1

print(result)

