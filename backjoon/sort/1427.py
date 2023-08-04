# 1427번 소트인사이드
# https://www.acmicpc.net/problem/1427


# 버블정렬 연습
def bubble_sort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 입력받은 숫자를 바로 배열로 변환한다.
arr = list(map(int, list(input())))
# sort 내장함수 지양, 버블정렬 사용
sorted_arr = bubble_sort(arr, len(arr))
# 출력할 때 역순으로 출력
[print(i, end="") for i in sorted_arr[::-1]]
