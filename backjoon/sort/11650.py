import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


# sort 지양, 버블 정렬 연습
# tuple의 경우 첫번째 인덱스의 값이 같을 때 다음 인덱스를 비교한다.
def bubble_sort(input_arr, length):
    for i in range(length-1, 0, -1):
        for j in range(i):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j]
    return input_arr


arr = []
N = int(input())
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

sorted_arr = bubble_sort(arr, N)
[print(*i) for i in sorted_arr]
