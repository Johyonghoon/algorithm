# 1780번 종이의 개수
# https://www.acmicpc.net/problem/1780

"""
가장 최소 단위인 3 * 3 부터 탐색하면서 같은 수로 채워진 배열의 경우
3 * 3의 배열을 1의 배열로 줄이는 방식으로 개수를 추가해간다.

"""
from collections import defaultdict


def shrink(arr):
    global cnt_minus, cnt_zero, cnt_plus
    new_arr = [[0 for _ in range(len(arr)//3)] for _ in range(len(arr)//3)]
    for y in range(0, len(arr), 3):
        for x in range(0, len(arr), 3):
            numbers = defaultdict(int)
            for ey in range(3):
                for ex in range(3):
                    numbers[arr[y+ey][x+ex]] += 1
            if 9 in numbers.values():
                new_arr[y//3][x//3] = list(numbers)[0]
            else:
                cnt_minus += numbers[-1]
                cnt_zero += numbers[0]
                cnt_plus += numbers[1]
                new_arr[y//3][x//3] = 9

    return new_arr


import sys
input = sys.stdin.readline


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

sqr = 0
while N != 1:
    N //= 3
    sqr += 1

cnt_zero = 0
cnt_plus = 0
cnt_minus = 0

for _ in range(sqr):
    graph = shrink(graph)

# 모든 숫자가 같을 때
number = graph[0][0]

if number == 0:
    cnt_zero += 1
elif number == 1:
    cnt_plus += 1
elif number == -1:
    cnt_minus += 1

print(cnt_minus)
print(cnt_zero)
print(cnt_plus)
