from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))
num_dict = defaultdict(int)
for i in range(n):
    num_dict[a[i]] += 1
for i in range(n):
    Aj = a[i] - x
    # Ai=Ajの場合を考慮
    if Aj == a[i]:
        if num_dict[Aj] > 1:
            print("Yes")
            quit()
    if num_dict[Aj] > 0:
        print("Yes")
        quit()
print("No")
