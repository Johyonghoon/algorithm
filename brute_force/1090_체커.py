# 1090번 체커
# https://www.acmicpc.net/problem/1090

coordinate = []
arr_x = []
arr_y = []
n = int(input())
result = [int(1e9) for _ in range(n+1)]
result[:2] = [0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])
    arr_x.append(x)
    arr_y.append(y)

arr_x.sort()
arr_y.sort()

for x in arr_x:
    for y in arr_y:
        dist = []
        for ex, ey in coordinate:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)
        dist.sort()
        for a in range(2, n+1):
            if sum(dist[:a]) < result[a]:
                result[a] = sum(dist[:a])

for i in range(1, n+1):
    print(result[i], end=' ')


"""
for i in range(min(arr_x), max(arr_x) + 1):
    for j in range(min(arr_y), max(arr_y) + 1):
"""

"""
예를 들어, 리스트 요소의 개수가 6개일 때 4개의 인덱스를 가지는 리스트를 모두 구하여 평균과의 차이의 합을 구하는 방법은 뭘까?
"""