n, m, t = map(int, input().split())
ab = []
for i in range(m):
    ai, bi = map(int, input().split())
    ab.append([ai, bi])
end = 0
v = n
for i in range(m):
    v -= ab[i][0] - end
    if v <= 0:
        print("No")
        quit()
    v = min(v + ab[i][1] - ab[i][0], n)
    end = ab[i][1]

print("Yes") if v - (t - end) > 0 else print("No")
