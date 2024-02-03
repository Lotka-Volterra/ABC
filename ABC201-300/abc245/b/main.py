n = int(input())
a = list(map(int, input().split()))
seta = sorted(list(set(a)))
for i in range(0, 2002):
    if i not in seta:
        print(i)
        quit()
