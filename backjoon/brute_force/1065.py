# 1065번 한수
# https://www.acmicpc.net/problem/1065

number = input()
arr = list(map(int, number))

# 내장함수 지양
length = 0
for _ in arr:
    length += 1

# 한수의 개수를 두자리 숫자의 최대값으로 설정
# 두자리 숫자까지는 무조건 한수
if length < 3:
    result = number
else:
    result = 99

    # 입력되는 수 1000은 이미 한수가 아니므로 1000에 대한 연산은 필요없다.
    # 세자리 수의 경우 3번째 수와 2번째 수의 차이가 2번째 수와 1번째 수의 차이가 같다면 한수
    for idx in range(100, int(number)+1):
        a = list(map(int, str(idx)))
        if a[1] - a[0] == a[2] - a[1]:
            result += 1

print(result)
