arr = ['1 10', '9 1', '1 9', '1 1', '9 9', '10 1']
print("정렬하지 않은 상태", arr)

arr.sort()
print("문자열 상태로 정렬", arr)

int_arr = []
for num in arr:
    int_arr.append(list(map(int, num.split())))
int_arr.sort()
print("int 자료형 출력 ", int_arr)


"""
# output
정렬하지 않은 상태 ['1 10', '9 1', '1 9', '1 1', '9 9', '10 1']
문자열 상태로 정렬 ['1 1', '1 10', '1 9', '10 1', '9 1', '9 9']
int 자료형 출력  [[1, 1], [1, 9], [1, 10], [9, 1], [9, 9], [10, 1]]
"""
