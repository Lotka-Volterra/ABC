n = int(input())
a = list(map(int, input().split()))
num = [0] * (10**5 + 2)
for i in range(n):
    num[a[i]] += 1
    num[a[i] + 1] += 1
    num[a[i] + 2] += 1
print(max(num))
