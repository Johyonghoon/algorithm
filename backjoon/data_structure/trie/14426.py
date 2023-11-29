# 14426번 접두사 찾기
# https://www.acmicpc.net/problem/14426

"""
얕은 복사를 역이용해서 문자열의 i번째 문자가 존재하는지 확인하면서 없다면 저장하기
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tri = dict()
for _ in range(N):
    string = list(input().strip())
    target = tri
    for i in range(len(string)):
        if string[i] not in target:
            target[string[i]] = dict()
        target = target[string[i]]
    # print(trie)

result = 0
for _ in range(M):
    string = list(input().strip())
    target = tri
    for i in range(len(string)):
        if string[i] not in target:
            # print(string, i)
            break
        target = target[string[i]]
    else:
        result += 1

print(result)
