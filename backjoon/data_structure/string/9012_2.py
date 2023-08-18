# 9012번 괄호
# https://www.acmicpc.net/problem/9012

T = int(input())
for _ in range(T):
    ps = input()
    N = len(ps)

    # 배열에 할당하여 모두 지워지지 않는다면 실패
    arr = []
    # 아래 과정에서 불가능한 상황 발생 시 False 할당
    isPossible = True
    for p in ps:
        # 왼쪽 괄호 나온다면 배열에 추가
        if p == "(":
            arr.append(p)
        # 오른쪽 괄호가 나올 때 배열이 비어있거나 왼쪽 괄호가 없다면 실패, 있다면 제거
        elif p == ")":
            if arr and arr[-1] == "(":
                arr.pop()
            else:
                isPossible = False
                break

    if not isPossible or len(arr) != 0:
        print("NO")
    else:
        print("YES")
