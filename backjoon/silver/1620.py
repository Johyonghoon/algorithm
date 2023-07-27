# 1620번 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

# value 값으로도 key 를 찾기 위해 둘 다 만들어 줌
pokemon_name = defaultdict()
pokemon_num = defaultdict()
for idx in range(1, N+1):
    name = input().strip("\n")
    pokemon_name[name] = idx
    pokemon_num[idx] = name

# 숫자일 경우와 문자일 경우를 구분하여 풀이
for _ in range(M):
    quiz = input().strip("\n")
    if quiz.isdecimal():
        print(pokemon_num[int(quiz)])
    else:
        print(pokemon_name[quiz])
