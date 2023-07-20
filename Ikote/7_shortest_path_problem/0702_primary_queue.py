import heapq

# 오름차순 정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 내림차순 정렬
def heapsort_descending(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
result = heapsort_descending([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)