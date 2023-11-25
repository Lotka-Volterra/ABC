s = "0123456789ABCDEF"

n = int(input())
sho = n // 16
sho2 = n - 16 * sho
print(s[sho] + s[sho2])
