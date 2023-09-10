a, b = map(int, input().split())
if a % 3 != 0 and b - a == 1:
    print("Yes")
else:
    print("No")
