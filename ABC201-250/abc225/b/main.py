n = int(input())
tree = [0] * n
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a - 1] += 1
    tree[b - 1] += 1
for i in range(n):
    if tree[i] == n - 1:
        print("Yes")
        quit()
print("No")
