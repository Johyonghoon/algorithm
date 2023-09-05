# 2467번 용액
# https://www.acmicpc.net/problem/2467

N = int(input())
numbers = list(map(int, input().split()))

start = 0
end = len(numbers)-1
mini = 2_000_000_000
result = []
while start < end:
    if mini > abs(numbers[end] + numbers[start]):
        mini = abs(numbers[end] + numbers[start])
        result = [numbers[start], numbers[end]]
    if abs(numbers[end-1] + numbers[start]) <= abs(numbers[end] + numbers[start+1]):
        end -= 1
    else:
        start += 1

print(*result)


"""
-99 -2 -1 4 98
-99 98
-99 4 -95
-2 98 -
"""