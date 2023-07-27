# 18110번 solved.ac
# https://www.acmicpc.net/problem/18110
import sys
input = sys.stdin.readline


def roundTraditional(val, digits):
    return int(round(val+10**(-len(str(val))-1), digits))


n = int(input())

# 아무 의견이 없다면 난이도는 0
if n == 0:
    print(0)
else:
    rank = []
    for _ in range(n):
        rank.append(int(input()))
    rank.sort()

    # python의 round는 특이하게 동작한다
    cut = roundTraditional(n / 100 * 15, 0)
    total = sum(rank[cut:n-cut])
    avg = roundTraditional(total / (n - 2 * cut), 0)

    print(avg)

"""
20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

output
11

일반적인 round 함수 사용 시
10 출력
"""