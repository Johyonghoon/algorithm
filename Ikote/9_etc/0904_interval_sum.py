def interval_sum(n, arr, x, y):
    sum_value = 0
    prefix_sum = [0]
    for i in arr:
        sum_value += i
        prefix_sum.append(sum_value)
    left = x
    right = y
    print(prefix_sum[right] - prefix_sum[left - 1])


if __name__ == '__main__':
    # n = 5 / arr = [10, 20, 30, 40, 50] / x = 3 / y = 4
    n = int(input("데이터의 개수 n을 입력하세요 : "))
    arr = list(map(int, input("배열을 입력하세요 : ").split()))
    x, y = map(int, input("찾고자 하는 x번째 ~ y번째 수의 합에 해당하는 x, y 값을 입력하세요 : ").split())
    interval_sum(n, arr, x, y)
