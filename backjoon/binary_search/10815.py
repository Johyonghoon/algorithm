# 10815번 숫자 카드
# https://www.acmicpc.net/problem/10815

n = int(input())
array_n = sorted(list(map(int, input().split())))
m = int(input())
array_m = list(map(int, input().split()))
result = []


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


for i, j in enumerate(array_m):
    result[i] = binary_search(array_n, j, 0, n-1)


print(*result)
