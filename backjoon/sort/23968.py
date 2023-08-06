# 23968번 알고리즘 수업 - 버블 정렬 1
# https://www.acmicpc.net/problem/23968
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))


def bubble_sort(a, length, k):
    cnt = 0
    for i in range(length-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt += 1
                if cnt == k:
                    return a[j], a[j+1]
    return -1, -1

small, big = bubble_sort(arr, N, K)
if small == -1 and big == -1:
    print(-1)
else:
    print(small, big)
