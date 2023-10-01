l, h = map(int, input().split())
n = int(input())
for i in range(n):
    hour = int(input())
    if hour > h:
        print(-1)
    else:
        print(max(0, l - hour))
