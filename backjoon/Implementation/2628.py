# 2628번 종이자르기
# https://www.acmicpc.net/problem/2628


width, height = map(int, input().split())
N = int(input())
X = [0, width]
Y = [0, height]
for _ in range(N):
    arr = list(map(int, input().split()))
    # 세로로 자를 때 :: X축을 기점으로 나누어 짐
    if arr[0]:
        X.append(arr[1])

    # 가로로 자를 때 :: Y축을 기점으로 나누어 짐
    else:
        Y.append(arr[1])

X.sort()
Y.sort()

# print(X, Y)

maxi = 0
# 인덱스 범위의 변의 길이를 가진 직사각형의 너비 구하기
for i in range(len(Y)-1):
    for j in range(len(X)-1):
        vol = (Y[i+1] - Y[i]) * (X[j+1] - X[j])
        maxi = max(maxi, vol)

print(maxi)


