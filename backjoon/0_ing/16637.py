# 16637번 괄호 추가하기
# https://www.acmicpc.net/problem/16637

"""
길이가 N인 수식에 정수와 연산자(+, -, x)로 이루어져 있다.
연산자의 우선순위는 모두 동일하여, 순차적으로 계산
이 수식에 괄호를 적절히 사용하여 결과값을 최대로 하는 문제
문제 조건에 의해 괄호 안의 괄호(중첩)는 불가능하다.
연산을 시작하기 전에, 우선순위가 높은 연산을 먼저 설정한다.
이때, 연속한 순서의 연산은 연달아 우선순위를 높일 수 없다.
(한 숫자가 두 개의 괄호 안에 들어 갈 수 없기 떄문)
[3, 8, 7, 9, 2]
[+, *, -, *]
[11 0 0 0]

"""


def operate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    elif op == "-":
        return num1 - num2


def leftover():
    global result

    # print("dp", dp)
    # print("numbers", numbers)
    # print("ops", ops)

    number = numbers[0]
    # dp의 경우 다음 연산을 이미 계산했다는 것을 저장
    is_early = False
    for k in range(L):
        if is_early:
            is_early = False
            continue
        if k+1 != L and dp[k+1] != int(1e9):
            is_early = True
            number = operate(number, dp[k+1], ops[k])
        else:
            number = operate(number, numbers[k+1], ops[k])

    # print("number", number)
    result = max(result, number)
    return


def first_op(node):
    if node >= L:
        leftover()
        return

    for j in range(node, L):
        # 직전에 우선 연산이 이루어진 경우 괄호가 중첩되어 불가능하다
        if dp[j-1] == int(1e9):
            num1 = numbers[j]
            num2 = numbers[j+1]
            op = ops[j]

            dp[j] = operate(num1, num2, op)
            first_op(j+1)
            dp[j] = int(1e9)
    else:
        first_op(L)


N = int(input())
arr = list(input())

ops = []
numbers = []
for idx in range(N):
    if idx % 2:
        ops.append(arr[idx])
    else:
        numbers.append(int(arr[idx]))

result = -(int(1e9))
# 미리 연산을 했을 때 그 결과를 저장
L = len(ops)
# 연산 결과가 0이 될 수도 있어서 0으로 저장해서는 안된다...
dp = [int(1e9) for _ in range(L)]
# 괄호 안에 1번이라도 들어 갔다면 다시는 우선 연산이 될 수 없다.
# 0번째 인덱스는 첫 번째 연산이므로 괄호를 하나마나 결과는 안한 것과 같다.
# 따라서, 1번째 인덱스 부터 탐색
first_op(1)

print(result)
