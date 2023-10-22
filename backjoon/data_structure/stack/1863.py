# 1863번 스카이라인 쉬운거
# https://www.acmicpc.net/problem/1863

"""
# 스택/그리디
스카이라인은 해가 질 때 그림자 지는 건물의 실루엣을 의미한다.
특정 높이 이상의 건물이 새로 나타나거나 사라질 때 건물의 새로운 시작과 끝을 알 수 있다.
즉, 현재 높이보다 높은 건물이 나타나는 것만 알 수 있는 것이다.
스택과 그리디 관점으로 해결 가능할 것 같다.
"""

N = int(input())
stack = []
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
    if stack and stack[-1] == y:
        continue
    if y:
        stack.append(y)
        cnt += 1


print(cnt)
