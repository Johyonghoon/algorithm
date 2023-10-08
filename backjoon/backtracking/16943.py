# 16943번 숫자 재배치
# https://www.acmicpc.net/problem/16943

"""
A의 숫자를 섞어 B보다 작은 수중 가장 큰 새로운 수 C를 만드는 문제

A 숫자의 길이가 B보다 길다면 불가능
"""


def recur(node, arr, isTrue):
    global result
    if node == N:
        num_arr = [numbers[i] for i in arr]
        # print(num_arr)
        C = int("".join(num_arr))
        if C < B:
            result = C
            return

    for idx in range(N):
        if result:
            return
        if idx in arr:
            continue
        if node == 0:
            if numbers[idx] == '0':
                continue
        # 새로운 배열에 들어가는 수가 반드시 B보다 작지 않을 때
        if not isTrue:
            # 해당 인덱스의 수가 B 인덱스의 수보다 크다면 패스
            if numbers[idx] > target[node]:
                continue
            # 작다면
            elif numbers[idx] < target[node]:
                recur(node+1, arr+[idx], True)
        recur(node+1, arr+[idx], isTrue)


A, B = map(int, input().split())
numbers = list(str(A))
target = list(str(B))
numbers.sort(reverse=True)
N = len(numbers)
M = len(target)

result = 0
if N == M:
    recur(0, [], False)
elif N < M:
    result = int("".join(numbers))

if result:
    print(result)
else:
    print(-1)

"""
9876534221 1234567890
"""
