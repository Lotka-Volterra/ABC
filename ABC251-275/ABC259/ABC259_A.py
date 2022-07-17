n, m, x, t, d = map(int, input().split())
zerosai = t-d*x
print(min(zerosai+d*m, zerosai+d*x))
