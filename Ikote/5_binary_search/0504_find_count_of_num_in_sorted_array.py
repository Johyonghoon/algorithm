from bisect import bisect_right, bisect_left


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


if __name__ == '__main__':
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    count = count_by_range(array, x, x)
    if count == 0:
        print(-1)
    else:
        print(count)
