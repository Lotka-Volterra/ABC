n = int(input())
a = list(map(int, input().split()))
odd = []
even = []
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
odd.sort(reverse=True)
even.sort(reverse=True)
oddans = -1 if len(odd) < 2 else odd[0] + odd[1]
evenans = -1 if len(even) < 2 else even[0] + even[1]
print(max(oddans, evenans))
