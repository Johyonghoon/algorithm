# 7696번 반복하지 않는 수
# https://www.acmicpc.net/problem/7696


while True:
    n = int(input())

    # 0이 입력될 경우 종료
    if n == 0:
        break

    cnt = 0
    i = 0
    while True:
        i += 1
        s = str(i)
        for idx in range(len(s)-1):
            if idx + 1 >= len(s):
                break
            if s[idx] == s[idx+1]:
                break
        else:
            cnt += 1
            if cnt == n:
                break

    print(i)








"""
# 시간초과

while True:
    n = 0
    cnt = 0
    N = int(input())
    if N == 0:
        break
    while True:
        n += 1
        if n > 10:
            breaky = False
            d = defaultdict(int)
            temp = str(n)
            for i in temp:
                if temp.count(i) > 1:
                    breaky = True
                    break
            if breaky:
                continue
        cnt += 1
        if cnt == N:
            break
    if cnt == N:
        print(n)
        continue
"""