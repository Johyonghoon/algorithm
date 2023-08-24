# 3985번 롤 케이크
# https://www.acmicpc.net/problem/3985

L = int(input())
# 실제 할당되는 케이크
cake = [0 for _ in range(L+1)]

N = int(input())
# 원하는 개수
want = [0 for _ in range(N+1)]
for idx in range(1, N+1):
    s, e = map(int, input().split())
    want[idx] = e - s + 1
    for j in range(s, e+1):
        if cake[j]:
            continue
        cake[j] = idx

# 결과 출력
maxi_cnt = 0
maxi_num = 0
for idx, num in enumerate(want):
    if maxi_cnt < num:
        maxi_cnt = num
        maxi_num = idx
print(maxi_num)

# 실제 할당 개수
real = [0 for _ in range(N+1)]
for num in cake:
    real[num] += 1

real_cnt = 0
real_num = 0
for idx, num in enumerate(real):
    if idx == 0:
        continue
    if real_cnt < num:
        real_cnt = num
        real_num = idx

print(real_num)
