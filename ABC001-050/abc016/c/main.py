n, m = map(int, input().split())
friends = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a - 1].add(b - 1)
    friends[b - 1].add(a - 1)
for i in range(n):
    ans = set()
    for j in friends[i]:
        ans = ans.union(friends[j])
    notFriends = set(friends[i])
    notFriends.add(i)
    print(len(ans - notFriends))
