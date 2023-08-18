# 2941번 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

string = input()
N = 0  # len_string
for _ in string:
    N += 1

# 결과 초기화
result = 0

# 다음 알파벳을 확인하여 크로아티아 알파벳으로 변환했다면
# 알파벳 길이만큼 idx 를 증가시킴
# 문자열의 길이가 2라면 idx += 2, 길이가 3이라면 idx += 3
idx = 0
while idx < N:
    if idx + 1 < N:
        if string[idx] == "c":
            if string[idx+1] == "=":
                result += 1
                idx += 2
                continue
            elif string[idx+1] == "-":
                result += 1
                idx += 2
                continue
        elif string[idx] == "d":
            if string[idx+1] == "z":
                if idx + 2 < N and string[idx+2] == "=":
                    result += 1
                    idx += 3
                    continue
            elif string[idx+1] == "-":
                result += 1
                idx += 2
                continue
        elif string[idx] == "l":
            if string[idx+1] == "j":
                result += 1
                idx += 2
                continue
        elif string[idx] == "n":
            if string[idx+1] == "j":
                result += 1
                idx += 2
                continue
        elif string[idx] == "s":
            if string[idx+1] == "=":
                result += 1
                idx += 2
                continue
        elif string[idx] == "z":
            if string[idx+1] == "=":
                result += 1
                idx += 2
                continue
    # 아무 조건에 걸리지 않을 경우
    result += 1
    idx += 1

print(result)
