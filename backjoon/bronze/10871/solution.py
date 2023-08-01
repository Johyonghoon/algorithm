# 10871번 X보다 작은 수
# https://www.acmicpc.net/problem/10871
import sys
sys.stdin = open("input.txt")


N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 만약 number 가 X보다 작다면 출력하기
for number in arr:
    if number < X:
        print(number, end=" ")
