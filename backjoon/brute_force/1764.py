# 1764번 듣보잡
# https://www.acmicpc.net/problem/1764

# import sys
#
# input = sys.stdin.readline

N, M = map(int, input().split())
arr_N = []
arr_M = []
for _ in range(N):
    arr_N.append(input())
for _ in range(M):
    arr_M.append(input())
arr_N.sort()
arr_M.sort()
result = []

n, m = 0, 0
while n != N and m != M:
    n_name = arr_N[n]
    m_name = arr_M[m]
    if n_name == m_name:
        result.append(n_name)
        n += 1
        m += 1
    else:
        i = 0
        while str(n_name)[i] == str(m_name)[i]:
            if len(n_name) == i+1 or len(m_name) == i+1:
                if len(n_name) > len(m_name):
                    m += 1
                    n -= 1
                break
            i += 1
        if str(n_name)[i] > str(m_name)[i]:
            m += 1
        else:
            n += 1

print(len(result))
[print(i) for i in result]
print(result)
"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhe
clinton
"""