# 11170번 0의 개수
# https://www.acmicpc.net/problem/11170
# import sys
# sys.stdin = open("input.txt")


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # 0의 개수
    cnt_zero = 0
    # N부터 M까지의 숫자를 리스트로 변환하여 "0"의 개수 찾기
    for number in range(N, M+1):
        arr = list(str(number))
        for string in arr:
            if string == "0":
                cnt_zero += 1

    print(cnt_zero)
