# 20546번 기적의 매매법
# https://www.acmicpc.net/problem/20546

# 잔액, 갯수
junhyun = [int(input()), 0]
sungmin = [junhyun[0], 0]
stock = list(map(int, input().split()))

updown = [0 for _ in range(14)]
for idx in range(1, 14):
    if stock[idx] - stock[idx-1] > 0:
        updown[idx] = 1
    elif stock[idx] - stock[idx-1] < 0:
        updown[idx] = -1

last = 0
for idx in range(14):
    price = stock[idx]
    if idx == 13:
        last = price

    junhyun[1] += junhyun[0] // price
    junhyun[0] %= price

    # 성민이가 주식을 가지고 있을 때
    if sungmin[1]:
        for j in range(3):
            if idx - j < 0:
                break
            if updown[idx-j] != 1:
                break
        else:
            sungmin[0] += sungmin[1] * price
            sungmin[1] = 0

    # 성민이가 주식이 없을 때
    else:
        for j in range(3):
            if idx - j < 0:
                break
            if updown[idx-j] != -1:
                break
        else:
            sungmin[1] = sungmin[0] // price
            sungmin[0] += sungmin[1] % price

    # print(idx+1, price, junhyun, sungmin)

junhyun_balance = junhyun[0] + junhyun[1] * last
sungmin_balance = sungmin[0] + sungmin[1] * last

# print(junhyun_balance)
# print(sungmin_balance)

if junhyun_balance > sungmin_balance:
    print('BNP')
elif junhyun_balance == sungmin_balance:
    print('SAMESAME')
else:
    print('TIMING')
