# 2745번 진법 변환
# https://www.acmicpc.net/problem/2745

N, B = input().split()

length = 0
for _ in N:
    length += 1

result = 0

for idx, s in enumerate(N[::-1]):
    if s.isalpha():
        num = ord(s) - ord("A") + 10
    else:
        num = int(s)
    result += num * (int(B) ** idx)

print(result)
