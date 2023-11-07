# 2596번 비밀편지
# https://www.acmicpc.net/problem/2596

"""
1. 6개 숫자를 문자로 바꾸는 규칙이 존재한다.
2. 만약 규칙에 해당하는 문자가 없다면, 단 하나의 숫자만 틀린 경우를 찾는다.
3. 약속이 잘 만들어져 있기 때문에 하나의 숫자만 틀리는 경우가 여러 개는 존재하지 않는다.
4. 만약, 여섯 숫자 중 두개 이상 모두 틀릴 경우에는 해당 문자의 위치를 출력한다.
"""


secrets = ["000000", "001111", "010011", "011100", "100110",
           "101001", "110101", "111010"]

# 비밀편지 저장
N = int(input())
arr = list(input())
letters = []
for idx in range(N):
    letters.append(arr[idx*6:(idx+1)*6])

result = ""
for i, letter in enumerate(letters):
    chrt = "".join(letter)
    # 이미 아는 문자 중에 있다면
    if chrt in secrets:
        result += chr(ord("A") + list(secrets).index(chrt))
    # 아는 문자 중에 없다면
    else:
        # 숫자를 비교하여 1개 이하로 틀릴 경우에만 저장하고 종료
        for idx, secret in enumerate(secrets):
            cnt = 0
            for j, num in enumerate(secret):
                if letter[j] != num:
                    cnt += 1
            if cnt < 2:
                result += chr(ord("A") + idx)
                break
        # 모든 비밀문자가 해당하지 않는다면 그런 것이 처음 나오는 위치를 저장
        # 파이썬은 타입이 달라져도 괜찮다.
        else:
            result = i+1
            break

print(result)
