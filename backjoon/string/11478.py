# 11478번 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

S = input()

N = 0
for _ in S:
    N += 1

# 딕셔너리에 부분 문자열 저장
d = {}
cnt = 0

for i in range(N):
    for j in range(i, N):
        if S[i:j+1] not in d:
            d[S[i:j+1]] = 1
            cnt += 1
        else:
            continue

print(cnt)
