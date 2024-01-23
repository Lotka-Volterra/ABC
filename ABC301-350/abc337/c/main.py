import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)


# class DoubleLinkedList:
#     class Node:
#         def __init__(self, data, previous=None, next=None):
#             self.data = data
#             self.previous = previous
#             self.next = next

#     def __init__(self):
#         self._head = self.Node("DUMMY-HEAD")
#         self._tail = self.Node("DUMMY-TAIL", previous=self._head)
#         self._head.next = self._tail
#         self.length = 0

#     def _search(self, data):
#         target = self._head.next
#         while True:
#             if target == self._tail:
#                 return None
#             if target.data == data:
#                 return target
#             target = target.next

#     # データを末尾に連結
#     def add(self, data):
#         node = self.Node(data, previous=self._tail.previous, next=self._tail)
#         self._tail.previous.next = node
#         self._tail.previous = node
#         self.length += 1

#     def remove(self, data):
#         target = self._search(data)
#         if target is None:
#             raise ValueError("削除対象が見つかりませんでした")
#         target.previous.next = target.next
#         target.next.previous = target.previous
#         del target
#         self.length -= 1

#     # data_iの後にdataを追加
#     def insert(self, deta_i, data):
#         target = self._search(deta_i)
#         if target is None:
#             raise ValueError("挿入元のデータが見つかりませんでした")
#         node = self.Node(data, previous=target, next=target.next)
#         target.next.previous = node
#         target.next = node
#         self.length += 1

#     def print_reverse(self):
#         node = self._tail.previous
#         while node != self._head:
#             print(node.data)
#             node = node.previous

#     def pophead(self):
#         target = self._head.next
#         if target == self._tail:
#             return None
#         self._head.next = target.next
#         target.next.previous = self._head
#         data = target.data
#         self.length -= 1
#         del target
#         return data

#     def poptail(self):
#         target = self._tail.previous
#         if target == self._head:
#             return None
#         self._tail.previous = target.previous
#         target.previous.next = self._tail
#         data = target.data
#         self.length -= 1
#         del target
#         return data

#     @property
#     def list(self):
#         node_data = []
#         node = self._head.next
#         while node != self._tail:
#             node_data.append(node.data)
#             node = node.next
#         return node_data

#     def __iter__(self):
#         node_data = self.list
#         return iter(node_data)


# dll = DoubleLinkedList()
n = int(input())
a = list(map(int, input().split()))
link = [0] * n
start = 0
for i in range(n):
    if a[i] == -1:
        # dll.add(i+1)
        start = i
    else:
        link[a[i] - 1] = i
ans = [start + 1]
for i in range(n):
    ans.append(link[start] + 1)
    start = link[start]
print(*ans[:-1])
