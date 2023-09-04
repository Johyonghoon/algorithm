# 11497번 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497

"""
정렬시킨 후 퐁당퐁당(홀수 짝수)으로 재정렬하여 두번째 배열은 역순으로 하면 최소가 되지 않을까?
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    even = []
    odd = []
    for idx in range(N):
        if idx % 2 == 0:
            even.append(arr[idx])
        else:
            odd.append(arr[idx])

    odd.reverse()
    new_arr = even + odd

    result = []
    for idx in range(N):
        result.append(abs(new_arr[idx] - new_arr[idx-1]))

    # print(new_arr)
    print(max(result))

