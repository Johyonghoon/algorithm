# 10166번 관중석
# https://www.acmicpc.net/problem/10166

"""
# 완전탐색 -> 메모리 초과
# 소수점 자리를 모두 탐색할 수 있는 방법이 뭐가 있을까
기약분수로 변경하여 저장하기
  - 기약분수 : 분모와 분자의 공약수가 1뿐인 분수, 더이상 약분되지 않는 분수
  - 최대공약수로 나누어 주면 된다. 최대공약수를 구하는 방법 : 유클리드 호제법

(시간초과 해결법) 일반적으로 전역변수에 접근하는 것보다 지역변수에 접근하는 시간이 조금 덜 걸린다.
             그렇기 때문에 함수로 선언하면 실행 시간을 조금 더 줄일 수 있다.
"""
import sys
from math import gcd
input = sys.stdin.readline

# # 유클리드 호제법
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a


def solve():
    D1, D2 = map(int, input().split())

    seats = [[0 for _ in range(D2+1)] for _ in range(D2+1)]
    cnt = 0
    for number in range(D1, D2+1):
        for idx in range(number):
            tmp = gcd(number, idx)
            y, x = number // tmp, idx // tmp
            if not seats[y][x]:
                seats[y][x] = 1
                cnt += 1

    print(cnt)


solve()
