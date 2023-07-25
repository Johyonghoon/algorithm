# 1654번 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline


def binary(ls, s, e, target):
    # 타겟에 해당되는 값이 복수개가 존재하므로 리스트에 저장하여 최댓값을 찾자
    ans = []
    while s <= e:
        middle = (s + e) // 2
        temp = sum(map(lambda x: x // middle, ls))
        if temp < target:
            e = middle - 1
        else:
            ans.append(middle)
            s = middle + 1
    return ans


K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

# 이분탐색 시도
print(max(binary(arr, 1, max(arr), N)))


"""
4 8
200
200
200
200

4 8
2
2
2
2
"""