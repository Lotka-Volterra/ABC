n, m = map(int, input().split())
n %= 12
choshin = n * 5
choshin += m / 12
kakudo = (max(choshin, m) - min(choshin, m)) * 6
print(min(kakudo, 360 - kakudo))
