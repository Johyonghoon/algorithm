# 1254번 팰린드롬 만들기
# https://acmicpc.net/problem/1254

"""
아래 아이디어를 생각해보면 어쩌면 아주 간단히 풀이할 수 있다.
문자열 길이만큼의 인덱스를 탐색하면 인덱스부터 문자열 끝까지의 문자가 팰린드롬이라면
해당 인덱스 이전까지의 길이만큼을 문자열 뒤에 추가해주면 팰린드롬을 충족하게 된다.
"""


def palindrome(string):
    if string == string[::-1]:
        return True
    return False


S = input()
N = len(S)
for idx in range(N):
    if palindrome(S[idx:]):
        print(N + idx)
        break


'''
문자열의 모든 문자를 탐색하며, 그 위치를 기준으로 이미 팰린드롬을 충족하는 문자의 개수를 저장
이때 왼쪽 또는 오른쪽 끝까지 팰린드롬이 충족해야 문자를 추가했을 때 팰린드롬을 만들 수 있다.
자기 자신이 팰린드롬의 기점이 되는 경우도 존재한다.

(문제 조건 유의) 문자열 "뒤"에 추가해서 팰린드롬을 만든다..
즉, 팰린드롬이 충족하는 문자열이 앞이 아닌 뒤에 도달해야 한다.
그래야, 팰린드롬 문자열 앞쪽에 충족하지 못한 문자열을 뒤에 추가할 수 있으니,,,


S = list(input())
# print(len(S))

cnts = [int(1e9) for _ in range(len(S))]

# 1. 자기 자신은 단독으로 존재하고, 좌우가 팰린드롬이 될 때
# 탐색범위를 중간부터 하는 이유는 좌측 벽에 먼저 도달하기 때문에 뒤에 문자열을 추가해도 충족할 수 없으므로,,,
start = len(S) // 2
for idx in range(start, len(S)):
    # 자기 자신을 포함한 팰린드롬을 충족하는 수의 개수
    cnt = 1
    for j in range(1, idx+1):
        # 좌우 탐색이 가능할 때
        if 0 <= idx - j and idx + j < len(S):
            # 팰린드롬을 충족한다면 충족하는 개수 저장
            if S[idx-j] == S[idx+j]:
                cnt += 2
            # 충족하지 않는다면 자기 자신을 제외하고 모두 추가해야 함
            else:
                cnt = 1
                break
    # 팰린드롬을 충족하는 문자열을 가지고 있다면 그만큼 제외하여 값을 반영하고 저장
    # 아니라면, 최대 문자열 길이만큼만 저장
    # 즉, 2 * len(S) - cnt
    cnts[idx] = min(cnts[idx], 2 * len(S) - cnt)

print(cnts)
# 2. 좌측 또는 우측에 자기 자신과 같은 문자열이 존재하여, 그 자체로 팰린드롬을 충족하고 시작할 떄
if len(S) % 2:
    start += 1
for idx in range(start, len(S)):
    if idx == 0:
        continue
    if S[idx-1] == S[idx]:

        # 자기 자신을 포함한 팰린드롬을 충족하는 수의 개수
        cnt = 2

        for j in range(1, idx+1):
            # 좌우 탐색이 가능할 때
            if 0 <= idx - 1 - j and idx + j < len(S):
                # 팰린드롬을 충족한다면 충족하는 개수 저장
                if S[idx-1-j] == S[idx+j]:
                    cnt += 2
                # 충족하지 않는다면 자기 자신을 제외하고 모두 추가해야 함
                else:
                    cnt = 2
                    break
        else:
            cnts[idx] = min(cnts[idx], 2 * len(S) - cnt)
            continue

# print(cnts)
print(min(cnts[len(S)//2:]))
'''



