# 1145번 적어도 대부분의 배수
# https://www.acmicpc.net/problem/1145

arr = list(map(int, input().split()))
ans = 0
while True:
    cnt = 0
    ans += 1
    for i in arr:
        if ans % i == 0:
            cnt += 1
    if cnt >= 3:
        break

print(ans)
