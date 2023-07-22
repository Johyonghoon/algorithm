# 1920번 수 찾기
# https://www.acmicpc.net/problem/1920

n = int(input())
arr_n = sorted(list(map(int, input().split())))
m = int(input())
arr_m = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for i, j in enumerate(arr_m):
    print(binary_search(arr_n, j, 0, n-1))
