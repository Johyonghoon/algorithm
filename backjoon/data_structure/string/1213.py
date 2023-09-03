# 1213번 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
from collections import defaultdict

name = list(input())
d = defaultdict(int)
for chrt in name:
    d[chrt] += 1

cnt = 0
words = set(name)
for word in words:
    if d[word] % 2 == 1:
        cnt += 1

if cnt <= 1:
    result = ""
    center_word = ""

    half_word = []
    for word, wcnt in d.items():
        if wcnt % 2 == 1:
            center_word = word
        for _ in range(wcnt//2):
            half_word.append(word)
    half_word.sort()
    result += "".join(half_word)
    result += center_word
    result += "".join(reversed(half_word))
    print(result)
else:
    print("I'm Sorry Hansoo")
