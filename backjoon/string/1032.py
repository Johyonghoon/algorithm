# 1032번 명령 프롬프트
# https://www.acmicpc.net/problem/1032

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(input())

# 내장함수 지양, 문자열 길이 확인
L = 0
for _ in arr[0]:
    L += 1

result = ""

# 모든 문자열에 같은 인덱스의 문자를 확인하여 다르다면 ? 할당, 아니라면 그 문자 할당
for x in range(L):
    chrt = ""
    for y in range(N):
        if y == 0:
            chrt = arr[y][x]
            continue
        if chrt != arr[y][x]:
            chrt = "?"
            break
    result += chrt

print(result)
