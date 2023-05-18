# 2439번 별찍기-2
# https://www.acmicpc.net/problem/2439

a = int(input())
for i in range(a):
	print(f"{' ' * (a - i - 1)}{'*' * (i + 1)}")