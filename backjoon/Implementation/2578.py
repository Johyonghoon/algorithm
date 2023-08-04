# 2578번 빙고
# https://www.acmicpc.net/problem/2578

"""
bingo_info = 숫자에 대한 빙고판 좌표 정보
bingo_ox = 빙고판이 채워졌는지에 대한 정보
numbers = 차례대로 읽는 수

1. 사회자가 순서대로 부르는 값의 위치에 True를 저장
2. 빙고판은 5 + 4 + 3 개의 수를 부른 후부터 3줄이 완성된다.
3. 12번째 숫자 이후로 줄이 완성됨을 확인하여 3개가 완성되었을 때
4. 몇번째인지 출력하고 종료

"""
# 빙고판 정보 입력
# 위치를 탐색해야 하므로 위치 정보를 별도로 저장
bingo_info = [[] for _ in range(26)]
for y in range(5):
    arr = list(map(int, input().split()))
    for x, num in enumerate(arr):
        bingo_info[num] = [y, x]

# 순서대로 읽는 번호 입력
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))
# print(numbers)


# 빙고를 확인!
def check_bingo(ls):
    bingo = 0
    # x축 전체 점검
    for ay in range(5):
        is_bingo = True
        for ax in range(5):
            if not ls[ay][ax]:
                is_bingo = False
        if is_bingo:
            bingo += 1
    # y축 전체 점검
    for bx in range(5):
        is_bingo = True
        for by in range(5):
            if not ls[by][bx]:
                is_bingo = False
        if is_bingo:
            bingo += 1
    # 대각선 점검
    is_bingo = True
    for i in range(5):
        if not ls[i][i]:
            is_bingo = False
    if is_bingo:
        bingo += 1
    # 역대각선 점검
    is_bingo = True
    for i in range(5):
        if not ls[i][4-i]:
            is_bingo = False
    if is_bingo:
        bingo += 1

    if bingo >= 3:
        return True
    else:
        return False


# 불리는 숫자에 대해 bingo_ox 판에 True 입력
bingo_ox = [[False for _ in range(5)] for _ in range(5)]
for idx, number in enumerate(numbers):
    ey, ex = bingo_info[number]
    bingo_ox[ey][ex] = True

    # 빙고판은 5 + 4 + 3 개의 수를 부른 후부터 3줄이 완성된다.
    # 12번째부터이므로, 11번 숫자 인덱스부터 확인
    if idx >= 11:
        if check_bingo(bingo_ox):
            # 출력은 0부터 시작하는 idx에 대해 +1 하여 출력
            print(idx+1)
            break
