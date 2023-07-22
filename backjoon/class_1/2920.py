# 2920번 음계
# https://www.acmicpc.net/problem/2920

a = input().split()
if a == sorted(a): print('ascending')
elif a == sorted(a, reverse=True): print('descending')
else: print('mixed')
