n = int(input())
a = list(map(int, input().split()))
print("Yes") if len(list(set(a))) == 1 else print("No")
