# 21275번 폰 호석만
# https://www.acmicpc.net/problem/21275


num1, num2 = input().split()


# 10진수 숫자 찾기
def find_num(x):
    if x.isalpha():
        return ord(x) - ord("a") + 10
    else:
        return int(x)


def calculate(numbers, nmrc):
    n = 0
    for idx, number in enumerate(numbers[::-1]):
        n += find_num(number) * (nmrc ** idx)
    return n


# 입력 숫자의 최소 진법 찾기
# 자기 자신을 나타내는 숫자보다 1만큼 큰 수부터 진법으로 사용 가능
mini_numeric1 = find_num(sorted(num1, reverse=True)[0]) + 1
mini_numeric2 = find_num(sorted(num2, reverse=True)[0]) + 1

result = []
# 완전 탐색
for A in range(mini_numeric1, 37):
    for B in range(mini_numeric2, 37):
        # num 숫자들 중에 0이 포함되어 있다면, 최소 진법 수를 1로 판단하게 됨
        if A < 2 or B < 2:
            continue
        # 문제 조건) A != B
        if A != B:
            decimal_num1 = calculate(num1, A)
            decimal_num2 = calculate(num2, B)
            # 10진법의 두 수가 같을 때
            if decimal_num1 == decimal_num2:
                # 문제 조건) 2 ** 63 보다 작다면
                if 0 <= decimal_num1 < 2**63:
                    # 결과 저장
                    result.append([decimal_num1, A, B])

if result:
    if len(result) > 1:
        print("Multiple")
    else:
        print(*result[0])
else:
    print("Impossible")
