# 1268번 임시 반장 정하기
# https://www.acmicpc.net/problem/1268
import sys
input = sys.stdin.readline

"""
N = 학생 수 
1. 1~9반까지 존재하므로 각 학년별 반에 해당하는 학생 번호를 입력
2. 소속해있는 같은 반의 학생을 학생 번호에 맞는 배열에 할당
3. 가장 많은 수의 학생 수를 가진 배열의 학생 번호를 출력
"""

N = int(input())
# 1~5학년, 1~9반 정보를 입력하기 위한 배열 초기화. 0학년 / 0반은 채워지지 않는다.
room_num_by_grade = [[[] for _ in range(10)] for _ in range(6)]

# i번 학생의 반 정보 또한 저장한다.
# 0번째 인덱스를 비우기 위해 리스트 하나를 넣어둔다.
student_info = [[]]

for i in range(1, N+1):
    # i번째 학생은 input_data의 첫번째부터 다섯번째까지의 반 번호에 정보가 들어간다.
    arr = list(map(int, input().split()))
    student_info.append(arr)
    # j+1 : 학년 정보 / k : 반 정보 / i : 학생 번호
    for j, k in enumerate(arr):
        room_num_by_grade[j+1][k].append(i)

# 모든 학생들의 반이 배정되면, 각 번호의 학생들과 같은 반인 친구들의 목록을 취합한다.
friends = [set() for _ in range(N+1)]
for i, numbers in enumerate(student_info):
    for j, number in enumerate(numbers):
        for friend in room_num_by_grade[j+1][number]:
            friends[i].add(friend)

# 같은 반이 된 친구가 많은 학생 번호를 탐색
maxi = 0
class_monitor = 0

for i, flist in enumerate(friends):
    if maxi < len(flist):
        class_monitor = i
        maxi = max(maxi, len(flist))

print(class_monitor)
