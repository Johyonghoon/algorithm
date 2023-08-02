# 2693번 N번째 큰 수
# https://www.acmicpc.net/problem/2693
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


# 버블 정렬 연습하기
def bubble_sort(input_arr, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j]
    return input_arr


T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    sorted_arr = bubble_sort(arr, 10)
    # 정렬되어 있으므로 뒤에서 3번째 인덱스의 값이 3번째 큰 값
    print(sorted_arr[-3])
