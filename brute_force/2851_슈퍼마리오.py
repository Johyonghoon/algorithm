# 2851번 슈퍼마리오
# https://www.acmicpc.net/problem/2851

score = []
for _ in range(10):
    score.append(int(input()))
prefix = [i for i in score]
deference = [0 for _ in range(10)]
for i in range(1, 10):
    prefix[i] += prefix[i-1]

for i, total in enumerate(prefix):
    deference[i] = abs(total - 100)

if deference.count(min(deference)) <= 1:
    print(prefix[deference.index(min(deference))])
else:
    deference.reverse()
    prefix.reverse()
    print(prefix[deference.index(min(deference))])

