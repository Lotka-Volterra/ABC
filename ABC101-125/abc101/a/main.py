s = input()
total = 0
for i in range(4):
    if s[i] == "+":
        total += 1
    else:
        total -= 1
print(total)
#スマートに
for i in s:
    if i == "+":
        total += 1
    else:
        total -= 1
print(total)
#公式回答例
s = input()
print (s.count("+") - s.count("-"))