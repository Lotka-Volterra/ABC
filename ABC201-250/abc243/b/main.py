n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sameposition = 0
differentposition = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j] and i == j:
            sameposition += 1
        elif a[i] == b[j] and i != j:
            differentposition += 1
print(sameposition)
print(differentposition)
