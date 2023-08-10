# 2346번 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346

N = int(input())
arr = list(map(int, input().split()))
balloons = [(num, idx+1) for idx, num in enumerate(arr)]

# 인덱스 초기화(1번 풍선부터 터뜨리기)
i = 0
result = []
while len(balloons) > 1:
    # print(i, balloons, result)
    L = len(balloons)

    # 만양 0보다 작다면 balloons 배열의 뒤부터 움직이도록 L 더하기
    if i < 0:
        i += L
        continue
    # i가 L보다 크다면 0번째 인덱스로 이동하고 움직이기
    if i >= L:
        i -= L
        continue

    # 풍선을 터뜨리며 움직이는 수 찾기
    balloon = balloons.pop(i)
    result.append(balloon[1])
    move = balloon[0]  # 3
    # 자기 자신이 사라지므로 인덱스 또한 감소하여 1만큼 적게 이동
    if move > 0:
        i += move - 1
    # 자기 자신이 사라지더라도 뒤로 돌아가는 움직임은 변하지 않음
    else:
        i += move

result.append(balloons[0][1])
print(*result)
