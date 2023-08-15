# 1406번 에디터
# https://www.acmicpc.net/problem/1406

"""
insert 메서드는 시간복잡도가 O(N)이므로 시간초과 발생
슬라이싱 또한 시간복잡도가 같기 때문에 시간초과 발생
이중연결 리스트를 사용해야 함
"""
import sys
input = sys.stdin.readline

left = list(input().strip())
right = []      # right는 stack으로 자료가 역순으로 들어가 있음을 기억 해야 함

# 명령의 개수
M = int(input())
for _ in range(M):
    arr = list(input().strip().split())
    command = arr[0]

    if command == "P":
        string = arr[1]
        left.append(string)
    elif command == "L":
        if len(left) == 0:
            continue
        right.append(left.pop())
    elif command == "D":
        if len(right) == 0:
            continue
        left.append(right.pop())
    elif command == "B":
        if len(left) == 0:
            continue
        left.pop()

[print(i, end="") for i in left]
[print(i, end="") for i in right[::-1]]
