# 3986번 좋은 단어
# https://www.acmicpc.net/problem/3986

N = int(input())
cnt = 0
for _ in range(N):
    S = input()

    # stack으로 문자를 입력하여 가장 나중에 들어간 문자와 같다면 지우기
    # 만약 다른 문자가 입력된다면 push
    # 최종적으로 스택에 문자가 남아있다면 좋은 단어가 아니다.
    stack = []
    for s in S:

        # 스택이 비어 있거나, 입력된 마지막 문자와 s가 다르다면 push
        if not stack or stack[-1] != s:
            stack.append(s)

        # 스택이 비어 있지 않고, 입력된 마지막 문자와 s가 같다면 push
        elif stack and stack[-1] == s:
            stack.pop()

    if not stack:
        cnt += 1

print(cnt)
