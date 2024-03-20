n, k = map(int, input().split())
bunshi = 0
bunbo = n**3
bunshi += (k - 1) * 1 * (n - k) * 6
bunshi += 1 * 1 * (n - k) * 3
bunshi += (k - 1) * 1 * 1 * 3
bunshi += 1
print(bunshi / bunbo)
