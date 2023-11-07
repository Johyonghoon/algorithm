# 1157번 단어 공부
# https://www.acmicpc.net/problem/1157

string = input().upper()
counts = [0 for _ in range(26)]  # 알파벳 26개에 대한 정보 입력
maxi = 0

for alphabet in string:
    idx = ord(alphabet) - ord("A")
    counts[idx] += 1
    if maxi < counts[idx]:
        maxi = counts[idx]

# 최대 개수와 해당 인덱스 확인
cnt = 0
result = 0
for j in range(26):
    if counts[j] == maxi:
        result = j
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(result + ord("A")))

