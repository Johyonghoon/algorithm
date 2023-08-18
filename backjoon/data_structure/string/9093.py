# 9093번 단어 뒤집기
# https://www.acmicpc.net/problem/9093

T = int(input())
for _ in range(T):
    arr = list(input().split())

    # 띄어쓰기를 기준으로 단어를 뒤집어서 출력

    def rev(x):
        p = ""
        for c in x:
            p = c + p
        return p

    for string in arr:
        print(rev(string), end=" ")
    print()
