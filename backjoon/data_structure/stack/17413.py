# 17413번 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413

S = list(input())
# 뒤집어지는 문자열 저장
stack = []
result = []
isPass = False

for idx in range(len(S)):

    # 괄호가 닫힌다면 결과에 바로 반영 여부 제거
    if S[idx] == ">":
        result.append(S[idx])
        isPass = False

    # 태그가 종료될 때까지 idx 지나가기
    elif S[idx] != ">" and isPass:
        result.append(S[idx])

    # 괄호가 열린다면 쌓인 stack을 뒤집어 결과에 더해줌
    elif S[idx] == "<":
        result += reversed(stack)
        result.append("<")
        stack = []
        isPass = True

    # 공백이 나타난다면 이제까지 나온 stack을 뒤집어 결과에 더해주고 공백 처리
    elif S[idx] == " ":
        result += reversed(stack)
        result += " "
        stack = []

    # 나머지 값들은 스택에 저장
    else:
        stack.append(S[idx])

result += reversed(stack)
[print(i, end="") for i in result]
