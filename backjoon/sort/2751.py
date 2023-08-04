# 2751번 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys
# N개의 수만큼 input을 받으므로 시간을 줄이기 위해 readline 메서드 사용
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    pass
    # 시간복잡도가 O(n^2) 인 방법으로는 틀리는 문제이므로 퀵정렬 배운 후 다시!
"""
# 내장함수 사용
import sys

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
[print(i) for i in arr]

"""