# 11279번 최대 힙
# https://www.acmicpc.net/problem/11279

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


class MaxHeap:

    def __init__(self):
        self.FRONT = 1
        self.size = 0
        self.max_size = 100_001
        self.heap = [0 for _ in range(self.max_size)]

    def isLeaf(self, node):
        if self.size // 2 < node <= self.size:
            return True
        return False

    def parent(self, node):
        return node // 2

    def left_child(self, node):
        return node * 2

    def right_child(self, node):
        return node * 2 + 1

    def swap(self, fn, sn):
        self.heap[fn], self.heap[sn] = self.heap[sn], self.heap[fn]

    def insert(self, num):
        self.size += 1
        self.heap[self.size] = num
        idx = self.size
        while self.parent(idx) and self.heap[self.parent(idx)] < self.heap[idx]:
            self.swap(self.parent(idx), idx)
            idx = self.parent(idx)

    def max_heapify(self, node):
        # print(">> heapify", node, h.heap[:10], h.size)
        if not self.isLeaf(node):
            if self.heap[node] < self.heap[self.left_child(node)] or \
                    self.heap[node] < self.heap[self.right_child(node)]:
                if self.heap[self.left_child(node)] > self.heap[self.right_child(node)]:
                    self.swap(node, self.left_child(node))
                    self.max_heapify(self.left_child(node))
                else:
                    self.swap(node, self.right_child(node))
                    self.max_heapify(self.right_child(node))

    def extract_max(self):
        if self.size:
            popped = self.heap[self.FRONT]
            self.heap[self.FRONT] = self.heap[self.size]
            self.size -= 1
            if self.size:
                self.max_heapify(self.FRONT)
            return popped
        else:
            return 0


N = int(input())
h = MaxHeap()
for _ in range(N):
    x = int(input())
    # x가 0이 아닐 때, heap에 삽입
    if x:
        h.insert(x)
    else:
        print(h.extract_max())

    # print(x, h.heap[:10], h.size)

"""
29
1 
8 
3 
14
13 
2 
7 
12 
4 
10 
6 
5 
11 
9 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0
"""

