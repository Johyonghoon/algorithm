def two_pointer(n, m, arr):
    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += arr[end]
            end += 1

        if interval_sum == m:
            count += 1
        interval_sum -= arr[start]

    print(count)  # output : 3


if __name__ == '__main__':
    # n = 5 / m = 5 / arr = [1, 2, 3, 2, 5]
    n, m = map(int, input("데이터의 개수 n과 찾고자하는 부분합 m을 띄어쓰기로 구분하여 입력하세요 : ").split())
    arr = list(map(int, input("수열을 띄어쓰기로 구분하여 입력하세요 : ").split()))
    two_pointer(n, m, arr)
