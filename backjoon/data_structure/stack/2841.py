# 2841번 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
cnt = 0
stacks = [[] for _ in range(N+1)]
for _ in range(N):
    line, fret = map(int, input().split())

    # 이미 프렛을 누르고 있다면
    while stacks[line]:
        # 연주해야 하는 프렛일 때 패스
        if stacks[line][-1] == fret:
            break
        # 연주해야 하는 프렛보다 낮은 번호의 프렛이 눌러져 있으면 누르기
        elif stacks[line][-1] < fret:
            stacks[line].append(fret)
            cnt += 1
            break
        # 연주해야 하는 프렛보다 큰 번호가 눌러져 있으면 떼기
        else:
            stacks[line].pop()
            cnt += 1

    # 프렛이 눌러져 있지 않거나, 눌러진 프렛을 모두 떼어낸 경우
    # 눌러야 하는 프렛을 추가하고 카운트
    if not stacks[line]:
        stacks[line].append(fret)
        cnt += 1
    # print(stacks[line], cnt)

print(cnt)
