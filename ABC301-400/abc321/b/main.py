n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, 101):
    tempA = []
    tempA = a + [i]
    if sum(tempA) - max(tempA) - min(tempA) >= x:
        print(i)
        quit()
print(-1)
