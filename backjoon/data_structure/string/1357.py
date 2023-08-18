# 1357번 뒤집힌 덧셈
# https://www.acmicpc.net/problem/1357


X, Y = map(int, input().split())


# 숫자를 문자열로 변환, 뒤집어서 다시 숫자로 반환
def rev(x):
    rev_x = ""
    for i in str(x):
        rev_x = i + rev_x
    return int(rev_x)


print(rev(rev(X) + rev(Y)))
