# 13423번 Three Dots
# https://www.acmicpc.net/problem/13423

import sys

input = sys.stdin.readline

def binary(arr, s, e, target):
    while s <= e:
        middle = (s+e)//2
        if target == arr[middle]:
            return True
        elif target > arr[middle]:
            s = middle + 1
        else:
            e = middle - 1
    return False


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    start = 0
    center = 1
    cnt = 0
    while start != N-2:
        while center != N-1:
            target = 2 * arr[center] - arr[start]
            if target < arr[center + 1]:
                center += 1
                continue
            if target > arr[-1]:
                break
            if binary(arr, center+1, N-1, target):
                cnt += 1
            center += 1
        start += 1
        center = start + 1
    print(cnt)

"""     
-4 -1 0 2 4
1
10
-100000000 1 2 4 5 6 7 8 9 1010321234

    print("in")
            print(f"0. binary{s} {e} {target}")
            print(f"1. binary{s} {e} {target}")
            print(f"2. binary{s} {e} {target}")
    print("out")

            print(arr[start], arr[center], target)


import sys

input = sys.stdin.readline

def binary(arr, s, e, target):
    while s <= e:
        middle = (s+e)//2
        if target == arr[middle]:
            return True
        elif target > arr[middle]:
            s = middle + 1
        else:
            e = middle - 1
    return False


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    start = 0
    end = 2
    cnt = 0
    while start != N-2:
        while end != N:
            target = (arr[start] + arr[end]) / 2
            if binary(arr, start, end, target):
                cnt += 1
            end += 1
        start += 1
        end = start + 2
    print(cnt)


arr[center] - arr[start] == ans - arr[center]
ans = 2




"""