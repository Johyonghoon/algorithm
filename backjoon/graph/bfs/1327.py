# 1327번 소트 게임
# https://www.acmicpc.net/problem/1327

"""
1부터 N자리의 순열
어떤 수를 뒤집으면 그 수부터 오른쪽으로 K개의 수를 뒤집어야 한다.

K개의 수를 뒤집을 수 있는 모든 경우의 수를 탐색
탐색하며 생기는 순열을 문자열로 저장하여 이미 존재한다면 더이상 탐색하지 않음
N, K가 작으니 슬라이싱을 써서 배열을 변경하는 방식을 사용해도 시간초과 없이 가능하지 않을까?
"""

from collections import deque


def bfs():
    global is_true
    q = deque()
    q.append((numbers, -1, 1))
    dup.add("".join(numbers))
    while q:
        arr, prv, cnt = q.popleft()
        for idx in range(N-K+1):
            for j in range(idx+1):
                changed_arr = arr[:j] + list(reversed(arr[j:j+K])) + arr[j+K:]
                changed_numbers = "".join(changed_arr)
                if changed_numbers == sorted_numbers:
                    is_true = True
                    print(cnt)
                    return

                if changed_numbers not in dup:
                    dup.add(changed_numbers)
                    q.append((changed_arr, j, cnt+1))



N, K = map(int, input().split())
numbers = input().strip().split()
sorted_numbers = "".join([str(i) for i in sorted(numbers)])

if numbers == sorted(numbers):
    print(0)
else:
    is_true = False
    dup = set()
    bfs()

    if not is_true:
        print(-1)

