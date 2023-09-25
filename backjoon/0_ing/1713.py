# 1713번 후보 추천하기
# https://www.acmicpc.net/problem/1713

N = int(input())
R = int(input())
rcmds = list(map(int, input().split()))

frames = [[0, 0] for _ in range(N)]

for rcmd in rcmds:
    for idx, arr in enumerate(frames):
        cnt, num = arr
        if num == rcmd:
            frames[idx][0] += 1
            break
    else:
        frames.pop()
        frames.append([1, rcmd])
        frames.sort(reverse=True)

result = []
for cnt, student in frames:
    if student:
        result.append(student)

result.sort()
print(*result)
