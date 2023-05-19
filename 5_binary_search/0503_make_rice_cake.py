n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort(reverse=True)


def binary_search_loop(array, target, start, end):
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in array:
            if i >= mid:
                sum += (i - mid)
        if sum == target:
            return print(mid)
        elif sum > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


binary_search_loop(ls, m, 0, ls[0])
