# 12919번 A와 B 2
# https://www.acmicpc.net/problem/12919


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, string, acnt, bcnt):
    global isTrue, isTurn
    if node == L:
        # print(string, isTurn)
        if isTurn:
            string = string[::-1]
        if string == T:
            isTrue = True
        return

    for chrt in ["A", "B"]:
        if isTrue:
            break
        if chrt == "A":
            if acnt == at:
                continue
            acnt += 1
            tmp = string
            if isTurn:
                string = "A" + string
            else:
                string += "A"
            recur(node+1, string, acnt, bcnt)
            acnt -= 1
            string = tmp

        elif chrt == "B":
            if bcnt == bt:
                continue
            bcnt += 1
            tmp = string
            if isTurn:
                string = "B" + string
                isTurn = False
                recur(node+1, string, acnt, bcnt)
                isTurn = True
            else:
                string += "B"
                isTurn = True
                recur(node+1, string, acnt, bcnt)
                isTurn = False
            bcnt -= 1
            string = tmp


S = input().strip()
T = input().strip()

L = len(T)
isTrue = False
isTurn = False
a = S.count("A")
b = S.count("B")
at = T.count("A")
bt = T.count("B")
recur(len(S), S, a, b)

print(int(isTrue))
