# 4949번 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
import sys

while True:
    string = sys.stdin.readline().strip('\n')
    if string == '.':
        break
    else:
        arr = list(string)
        ls = []
        bracket = ['(', ')', '[', ']']

        for word in arr:
            if word in bracket:
                # 왼쪽 괄호가 나타나면 ls에 추가
                if word == '(' or word == '[':
                    ls.append(word)
                elif word == ')':
                    if ls:
                        if ls[-1] == '(':
                            ls.pop()
                        else:
                            ls.append(word)
                    else:
                        ls.append(word)
                else:
                    if ls:
                        if ls[-1] == '[':
                            ls.pop()
                        else:
                            ls.append(word)
                    else:
                        ls.append(word)

        # 반복문이 종료되었을 때 ls 가 남아있다면 균형잡히지 않은 것
        if ls:
            print("no")
        else:
            print("yes")
