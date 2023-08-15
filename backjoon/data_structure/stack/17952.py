# 17952번 과제는 끝나지 않아!
# https://www.acmicpc.net/problem/17952
import sys
input = sys.stdin.readline

N = int(input())
# 가장 최근의 과제를 먼저 수행하므로 stack 사용
stack = []
result = 0

# N분 동안 과제가 주어지거나 주어지지 않는다.
for _ in range(N):
    arr = list(map(int, input().split()))
    # 과제가 주어지지 않는 경우
    if len(arr) == 1:
        if stack:
            stack[-1][0] -= 1
            if stack[-1][0] == 0:
                result += stack.pop()[1]
        continue
    # 과제가 주어지는 경우
    minute, A, T = arr
    # 1분 만에 해결한다면 바로 점수를 획득하고 그 과제는 종료된다.
    if T > 1:
        stack.append([T-1, A])
    else:
        result += A

# 결과 출력
print(result)

