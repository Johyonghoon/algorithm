import sys
# sys.stdin = open("input.txt")
sys.stdin = open("input_1.txt")

# 30명의 제출 여부를 확인하기 위한 배열 생성 (0번째는 생략)
arr = [True] + [False for _ in range(30)]
for _ in range(28):
    arr[int(input())] = True

# 내지 않은 False 값을 가진 인덱스 출석번호를 순서대로 출력
for idx in range(31):
    if not arr[idx]:
        print(idx)
