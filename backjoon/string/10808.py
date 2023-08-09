# 10808번 알파벳 개수
# https://www.acmicpc.net/problem/10808

S = input()
cnt = [0 for _ in range(26)]
for string in S:
    num = ord(string) - ord('a')
    cnt[num] += 1

print(*cnt)
