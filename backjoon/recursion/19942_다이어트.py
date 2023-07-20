# 19942번 다이어트
# https://www.acmicpc.net/problem/19942

N = int(input())
arr = [0]
numbers = []
ls = []
minimum = list(map(int, input().split()))
for number in range(1, N+1):
    protain, fat, carbohydrate, vitamin, price = map(int, input().split())
    arr.append([number, protain, fat, carbohydrate, vitamin, price])

def recur(number, protain, fat, carbohydrate, vitamin, price):
    if number == N+1:
        if protain >= minimum[0] and fat >= minimum[1] and carbohydrate >= minimum[2] and vitamin >= minimum[3]:
            ls.append([price] + numbers)
        return

    numbers.append(number)
    recur(number+1, protain + arr[number][1], fat + arr[number][2],
          carbohydrate + arr[number][3], vitamin + arr[number][4], price + arr[number][5])
    numbers.pop()
    recur(number+1, protain, fat, carbohydrate, vitamin, price)

recur(1, 0, 0, 0, 0, 0)

if len(ls):
    ls.sort()
    print(ls[0][0])
    print(*ls[0][1:])
else:
    print(-1)

"""
3
0 0 0 10
0 0 0 10 1
0 0 0 5 1
0 0 0 5 0
output
1
1
"""
"""
3
0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
output
0
1 2 3
"""
