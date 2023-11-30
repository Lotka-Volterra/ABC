import itertools

s, k = input().split()
k = int(k)
s = list(s)
count = 0

for i in sorted(list(set(itertools.permutations(s)))):
    count += 1
    if count == k:
        print("".join(i))
