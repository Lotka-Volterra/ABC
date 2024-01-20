from collections import defaultdict

n = int(input())
dict = defaultdict(int)
for i in range(n):
    s = input()
    if dict[s] == 0:
        print(s)
    else:
        print(s + "(" + str(dict[s]) + ")")
    dict[s] += 1
