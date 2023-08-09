# 1439번 뒤집기
# https://www.acmicpc.net/problem/1439

S = input()

# 양쪽에서 범위를 좁혀가면서, 숫자가 변동된다면 그 구간의 모든 수를 뒤집고 다시 이동
i = 0
e = len(S)-1
cnt = 0
isChange = False
isDiff = False
while i <= e:

    # 두 수가 다르다면 변경 시작 // 나는 i를 높여가며 e 값을 변경하는 식으로 고민
    if S[i] != S[e]:
        i += 1
        isChange = True

    else:

        if i == e:
            if isChange:
                cnt += 1
            if isDiff:
                cnt += 1
            break

        if isDiff:
            cnt += 1
            isDiff = False

        if isChange:
            cnt += 1
            isChange = False

        i += 1
        e -= 1
        if S[i] != S[i-1] and S[e] != S[e+1]:
            isDiff = True

print(cnt)
