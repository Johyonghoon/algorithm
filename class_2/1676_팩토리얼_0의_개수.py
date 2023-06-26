# 1676번 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

N = int(input())
facto = 1
cnt = 0
for i in range(2, N+1):
    facto *= i

while facto % 10 == 0:
    cnt += 1
    facto = facto // 10

print(cnt)
