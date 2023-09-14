# 1927번 최소 힙
# https://www.acmicpc.net/problem/1927

"""
100_000개의 연산을 1초에 해결하려면
배열에 자연수를 넣고, 가장 작은 값을 출력하는 과정이 빨라야 한다.

힙(Heap) : 여러 값들 중 최댓값과 최솟값을 빠르게 찾기 위해 이진 트리로 구성된 자료구조
- 항상 완전 이진 트리 형태
- 부모의 값은 항상 자식들의 값보다 크거나, 작아야 하는 규칙
- 시간복잡도 O(logN)

최소 힙(Min heap) : 자식들의 값보다 작아야 한다.
최대 힙(Max heap) : 자식들의 값보다 커야 한다.

가장 작은 값을 출력하고, 그 값을 배열에서 제거

            1
    2               3
4       5       6       7
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def isLeaf(node):
    if size // 2 < node <= size:
        return True
    return False


def parent(node):
    return node // 2


def left_child(node):
    return node * 2


def right_child(node):
    return node * 2 + 1


def swap(f, s):
    heap[f], heap[s] = heap[s], heap[f]


def min_heapify(node):
    # print("before min heapify")
    # print("heap", heap, size)
    # print("isLeaf", isLeaf(node), node, size)
    if not isLeaf(node):
        # print("change", node, left_child(node), right_child(node))
        if heap[node] > heap[left_child(node)] or \
                heap[node] > heap[right_child(node)]:
            if heap[left_child(node)] < heap[right_child(node)]:
                swap(node, left_child(node))
                min_heapify(left_child(node))
            else:
                swap(node, right_child(node))
                min_heapify(right_child(node))

            # print("after min heapify", heap, size)


def insert(num):
    global size
    size += 1
    heap[size] = num
    node = size
    while heap[parent(node)] > heap[node]:
        swap(node, parent(node))
        node = parent(node)


def extract_min():
    global size
    if size > 0:
        popped = heap[1]
        heap[1] = heap[size]
        size -= 1
        if size:
            min_heapify(1)
        return popped
    else:
        return 0


N = int(input())
heap = [0 for _ in range(100_000)]
size = 0
for _ in range(N):
    x = int(input())
    # print("x", x)
    # x가 자연수라면, 배열에 x라는 값을 넣는 연산
    if x:
        insert(x)
    # x가 0이라면, 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
    else:
        print(extract_min())
    # print("heap", heap, size)

"""
# input
13
1
2
100
4
5
6
0
0
0
0
0
0
0

# ans
1
2
4
5
6
100
0

# wrong output
1
2
5
4
6
100
0

# input
11
1
3
2
4
0
5
0
0
0
0
0

# ans
1
2
3
4
5
0

# output
1
2
3
4
4
0

# input
17
1
2
3
4
5
6
7
8
0
0
0
0
0
0
0
0
0

# ans
1
2
3
4
5
6
7
8
0

"""





