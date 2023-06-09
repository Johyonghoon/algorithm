# 1090번 체커
# https://www.acmicpc.net/problem/1090

arr_x = []
arr_y = []
n = int(input())
result = [0 for _ in range(n+1)]
for _ in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

# for i in range(2, n+1):


"""
예를 들어, 리스트 요소의 개수가 6개일 때 4개의 인덱스를 가지는 리스트를 모두 구하여 평균과의 차이의 합을 구하는 방법은 뭘까?
"""