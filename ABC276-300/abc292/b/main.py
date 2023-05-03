n, q = map(int, input().split())
player = [0] * n
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        player[query[1] - 1] += 1
    elif query[0] == 2:
        player[query[1] - 1] += 2
    else:
        if player[query[1] - 1] == 2:
            print("Yes")
        else:
            print("No")
