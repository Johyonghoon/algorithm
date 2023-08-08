# 11718번 그대로 출력하기
# https://www.acmicpc.net/problem/11718

"""
input이 몇 줄 들어오는지 모를 때 어떻게 풀까에 대한 문제
대체로 입력 개수가 정해져 있는 문제만 풀어온 사람들에게 함정을 만든 문제
"""
while True:
    try:
        s = input()
        print(s)
    except EOFError:
        break
