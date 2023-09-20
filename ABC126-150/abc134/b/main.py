n, d = map(int, input().split())
count = 1
sightend = 1 + 2 * d
while sightend < n:
    sightend += 1 + 2 * d
    count += 1
print(count)
