import sys
sys.stdin = open("input.txt")

# 최대 15개의 글자, 5줄이 주어진다.
graph = [["" for _ in range(15)] for _ in range(5)]
# 입력되는 문자를 빈 문자열에 채워준다.
for idx in range(5):
    input_arr = list(input())
    # enumerate 연습
    for j, string in enumerate(input_arr):
        graph[idx][j] = string
        j += 1

# y축 우선으로 출력!
cnt = 0
for x in range(15):
    for y in range(5):
        print(graph[y][x], end="")
