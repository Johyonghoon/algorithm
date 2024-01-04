# 2661번 좋은수열
# https://www.acmicpc.net/problem/2661

"""
숫자 1, 2, 3으로만 이루어지는 수열
임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다.
그렇지 않은 수열이 좋은 수열이다.
"""


def dfs(idx, num):
    global is_done
    if idx == N:
        print(num)
        is_done = True
        return

    for i in ['1', '2', '3']:
        if is_done:
            break
        # 가능한 길이만큼 늘려가며 가능 여부 판단
        new_num = num + i
        for j in range(1, (idx+1)//2+1):
            if new_num[-j:] == new_num[-(j*2):-j]:
                break
        else:
            dfs(idx+1, num+i)


N = int(input())
is_done = False
dfs(1, "1")
