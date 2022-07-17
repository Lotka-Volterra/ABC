import collections
N = int(input())
B = []
for i in range(N):
    C = input()
    B.append(C)

c = collections.Counter(B)
print(c.most_common()[0][0])

#はじめて解いた茶diff
#https://note.nkmk.me/python-collections-counter/