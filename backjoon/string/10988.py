# 10988번 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988

def rev(x):
    p = ""
    for i in x:
        p = i + p
    return p


s = input()
if s == rev(s):
    print(1)
else:
    print(0)
