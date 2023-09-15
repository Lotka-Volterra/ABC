n, m = map(int, input().split())
problem = [[0, 0] for i in range((2 * 10) ** 5)]
ac = 0
wa = 0
for i in range(m):
    p, s = input().split()
    p = int(p)
    if problem[p - 1][0] == 0 and s == "AC":
        problem[p - 1][0] = 1
        ac += 1
        wa += problem[p - 1][1]
    elif problem[p - 1][0] == 0 and s == "WA":
        problem[p - 1][1] += 1
print(ac, wa)
