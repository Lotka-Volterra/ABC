s = input()
print(s[0:5], s[6:13], s[14:])

# 実装する
s = input()
sc = ""
for i in s:
    if i == ",":
        sc += ' '
    else:
        sc += i

# 関数を使う
s = input()
print(s.replace(',', ' '))
