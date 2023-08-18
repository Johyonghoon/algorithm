# 5622번 다이얼
# https://www.acmicpc.net/problem/5622

arr = list(input())
result = 0

# 각 알파벳의 범위에 대해 주어진 시간 값을 결과에 더해줌
# 문제 조건이 알파벳 대문자 입력 값만 주어지므로, 그에 대한 예상 값만 반영
for string in arr:
    num = ord(string)
    if num <= ord("C"):
        result += 3
    elif num <= ord("F"):
        result += 4
    elif num <= ord("I"):
        result += 5
    elif num <= ord("L"):
        result += 6
    elif num <= ord("O"):
        result += 7
    elif num <= ord("S"):
        result += 8
    elif num <= ord("V"):
        result += 9
    else:
        result += 10

print(result)
