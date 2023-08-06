# 10989번 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
d = defaultdict(int)
maxi = 0
for _ in range(N):
    input_data = int(input())
    d[input_data] += 1
    maxi = max(maxi, input_data)

for idx in range(maxi+1):
    if d[idx]:
        for _ in range(d[idx]):
            print(idx)



"""
# 메모리 초과 / 근데 전에 이런 방식으로 제출해서 정답이었는데...
import sys
input = sys.stdin.readline
dp = [0 for _ in range(10_001)]

# 수의 개수를 받고, 각 값에 대해 dp 리스트에 저장
N = int(input())
maxi = 0
for _ in range(N):
    input_data = int(input())
    dp[input_data] += 1
    maxi = max(maxi, input_data)

for num, cnt in enumerate(dp[:maxi+1]):
    if cnt:
        [print(num) for _ in range(cnt)]
"""

"""
# 메모리 초과
import sys
input = sys.stdin.readline


# 카운팅 정렬 연습
def counting_sort(a, k):

    # 데이터 원소의 범위
    count_arr = [0 for _ in range(k+1)]

    # 각 원소의 빈도 저장
    for i in a:
        count_arr[i] += 1

    # 중복된 원소가 있을 경우, 각 순서를 기억하기 위해 count_arr 업데이트
    for i in range(1, k+1):
        count_arr[i] += count_arr[i-1]

    # 정렬되는 배열 초기화
    result = [-1 for _ in range(len(a))]

    # count_arr를 참조하여 a 값을 정렬
    for i in a:
        count_arr[i] -= 1
        result[count_arr[i]] = i

    return result


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

[print(i) for i in counting_sort(arr, max(arr))]
"""

"""
# 메모리 초과
import sys
input = sys.stdin.readline

# 1 <= N <= 10_000_000
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 10_000번 인덱스까지 존재하는 배열 생성
# 각 배열의 숫자에 해당하는 인덱스 개수를 증가
sorted_arr = [0 for _ in range(10_001)]
# 메모리 초과를 방지하기 위해 출력할 최대값 구하기
maxi = 0
for num in arr:
    sorted_arr[num] += 1
    if maxi < num:
        maxi = num

# 개수만큼 숫자 출력
for number, cnt in enumerate(sorted_arr[:maxi+1]):
    if cnt:
        [print(number) for _ in range(cnt)]
"""