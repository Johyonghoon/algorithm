
ls = [(1, 2), (0, 2), (0, 1), (1, 3)]

def bubble_sort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort(ls, len(ls))
print(ls)

