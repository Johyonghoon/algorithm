# 11945번 뜨거운 붕어빵
# https://www.acmicpc.net/problem/11945
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
for _ in range(N):
    arr = list(input())
    # 반복문으로 시퀀스 자료형인 리스트를 역순으로 출력
    for num in arr[::-1]:
        print(num, end="")
    print()
