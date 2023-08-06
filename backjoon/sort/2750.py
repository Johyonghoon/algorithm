# 2750번 정렬하기
# https://www.acmicpc.net/problem/2750
import sys
input = sys.stdin.readline

# 정렬할 배열 만들기
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))


def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


sorted_arr = bubble_sort(arr, len(arr))
[print(i) for i in sorted_arr]
