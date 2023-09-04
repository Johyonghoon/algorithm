# 1038번 감소하는 수
# https://www.acmicpc.net/problem/1038

"""
감소하는 수는 자릿수가 늘어날 수록 될 수 있는 가능성이 낮아진다.
예를 들어, 한 자리 숫자의 경우 모든 수가 감소하는 수를 만족한다.
두 자리 숫자의 경우, 10의 자리 숫자보다 반드시 낮아야 하므로,
십의 자리 수가 커질 수록 개수는 증가한다.
백의 자리수는 마찬가지로 10의 자리는 100의 자리 수의 눈치를 봐야하고,
1의 자리 수는 10의 자리 수를 눈치를 봐야 한다.
하지만 두 자리 숫자를 탐색할 때 이미 가능한 경우의 수를 모두 탐색했으므로,
이를 활용하여 두 자리 숫자와 마지막 한 자리 숫자를 결합하여 탐색한다.
마찬가지로 네 자리 숫자는 세 자리 숫자를 탐색을 마쳤으므로,
이와 한 자리 숫자를 결합하여 찾아낸다.
이 방식으로 모두 찾아내어, 열 자리 수까지 모두 탐색한 후 저장하고
N번째 숫차를 출력하면 게임 종료
"""


def recur(node, arr):
    if node == 10:
        return

    new_prefix = []
    for number in arr:
        for idx in range(N):
            if number % 10 > idx:
                decrese_num = number * 10 + idx
                new_prefix.append(decrese_num)
                numbers.append(decrese_num)
            else:
                break

    recur(node+1, new_prefix)


N = int(input())
numbers = [num for num in range(10)]
prefix = [num for num in range(10)]
recur(0, prefix)

if len(numbers) <= N:
    print(-1)
else:
    print(numbers[N])
