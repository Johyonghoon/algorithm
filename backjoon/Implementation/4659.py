# 4659번 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
"""
1. 모음(a,e,i,o,u)를 반드시 포함
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
3. 같은 글자가 연속적으로 두 번 오면 안되나, ee와 oo는 허용
"""
aeiou = ["a", "e", "i", "o", "u"]
while True:
    password = input()
    # 종료 조건
    if password == "end":
        break

    # 가능 여부 저장
    isTrue = True

    # 1. 모음 포함 여부 확인
    for word in password:
        if word in aeiou:
            break
    else:
        isTrue = False

    # 2. 모음이 3개 혹은 자음이 3개 연속 오면 안됨
    idx = 0
    cnt = 0
    isAEIOU = False
    while idx < len(password):
        w = password[idx]
        if isAEIOU:
            if w in aeiou:
                cnt += 1
            else:
                isAEIOU = False
                cnt = 1
        else:
            if w in aeiou:
                isAEIOU = True
                cnt = 1
            else:
                cnt += 1
        if cnt == 3:
            isTrue = False
        idx += 1

    # 3. 두 개 이상의 문자가 연달아 나올 때
    for idx in range(len(password)-1):
        if password[idx] == password[idx+1]:
            if password[idx] == "e" or password[idx] == "o":
                continue
            isTrue = False

    if isTrue:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
