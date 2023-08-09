# 10610번 30
# https://www.acmicpc.net/problem/10610

# 수의 모든 자릿수를 배열에 할당
arr = list(map(int, input()))

# 배열의 수 중에 0이 있다면? 10의 배수
# 배열의 수의 합이 3의 배수라면? 3의 배수
total = 0
for num in arr:
    total += num

if total % 3 != 0:
    print(-1)
elif 0 not in arr:
    print(-1)
else:
    # 배열의 길이 확인
    N = 0
    for _ in arr:
        N += 1

    # 결과를 배열로 저장
    result = [0 for _ in range(N)]
    # 정렬 // 버블정렬 시간 초과
    sorted_arr = sorted(arr)
    # 역정렬
    descend_arr = sorted_arr[::-1]
    # 출력
    [print(i, end="") for i in descend_arr]

"""
N = int(input())
arr = list(map(int, list(str(N))))
arr.sort(reverse=True)
number = int("".join(str(i) for i in arr))
if sum(arr) % 3 == 0 and number % 10 == 0:
    print(number)
else:
    print(-1)
"""
"""
N = int(input())
arr = list(map(int, list(str(N))))
arr.sort(reverse=True)
result = []
answer = -1
breaky = False

def recur():
    global answer, breaky
    if len(result) == len(arr):
        number = int("".join(str(arr[i]) for i in result))
        if number % 30 == 0:
            answer = max(number, answer)
            breaky = True
        return
    for idx in range(len(arr)):
        if idx in result:
            continue
        result.append(idx)
        recur()
        if breaky:
            break
        result.pop()

recur()

print(answer)
"""
