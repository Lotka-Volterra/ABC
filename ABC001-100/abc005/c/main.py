from collections import deque

t = int(input())
n = int(input())
que = deque(map(int, input().split()))
# for i in range(q):
# que.append(int(input()))
m = int(input())
b = list(map(int, input().split()))
if n < m:
    print("no")
    quit()
for i in range(m):
    is_served = False
    while len(que) > 0:
        q = que.popleft()
        if q > b[i]:
            print("no")
            quit()
        if q <= b[i] <= q + t:
            is_served = True
            break
    if not is_served:
        print("no")
        quit()
print("yes")
