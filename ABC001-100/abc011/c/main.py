n = int(input())
ngs = [int(input()) for i in range(3)]
if n in ngs:
    print("NO")
    quit()
dp = [set() for i in range(101)]
dp[0].add(n)
for i in range(100):
    if len(dp[i]) == 0:
        print("NO")
        quit()
    for j in dp[i]:
        js = [j - 1, j - 2, j - 3]
        for k in js:
            if k == 0:
                print("YES")
                quit()
        for k in js:
            if k not in ngs:
                dp[i + 1].add(k)
print("NO")
