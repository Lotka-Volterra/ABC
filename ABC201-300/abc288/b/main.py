n, k = map(int, input().split())
hn = []
for i in range(n):
    if i<k:
        hn.append(input())
    else:
        input()
hn.sort()
for i in range(k):
    print(hn[i])
