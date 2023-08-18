# 10799번 쇠막대기
# https://www.acmicpc.net/problem/10799

brackets = list(input())
# 레이저 정보를 담은 배열 생성
arr = []
isJump = False
for idx in range(len(brackets)-1):
    if isJump:
        isJump = False
        continue
    if brackets[idx] == "(":
        if brackets[idx+1] == ")":
            arr.append("0")
            isJump = True
        else:
            arr.append("(")
    else:
        arr.append(")")
arr.append(brackets[-1])

# print(arr)
cnt = 0
result = 0
for bracket in arr:
    if bracket == "(":
        cnt += 1
        result += 1
    elif bracket == "0":
        result += cnt
    else:
        cnt -= 1

print(result)
