X = int(input())
cnt = 0
# X번째 수는 (1, 1) : 1개 (1, 2) (2, 1) : 2개 ...
# (x, y) 좌표에 대해 합이 유지되며 cnt 개수가 등차수열로 증가하는 것을 고려하여
# X를 초과할 때 그 시점을 기준으로 시작점을 설정
start = 1
# x y축의 합이 증가할수록 1, 2, 3, 4 ... 처럼 개수가 증가하면서 이어진다
for i in range(1, 1_000_000_000):
    if cnt + i >= X:
        start = i + 1
        break
    cnt += i

for total in range(start, 1_000_000_000):
    # x 좌표의 값을 1부터 total-1 까지!(y값의 최소가 1이 되기 위해)
    for x in range(1, total):
        # 두 수의 합이 홀수일 때, x가 1부터 시작
        if total % 2 == 1:
            result = f"{x}/{total-x}"
        # 두 수의 합이 짝수일 때, y가 1부터 시작
        else:
            result = f"{total-x}/{x}"
        cnt += 1
        if cnt == X:
            print(result)
            exit()
