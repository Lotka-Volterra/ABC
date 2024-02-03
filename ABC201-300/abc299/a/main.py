n = int(input())
s = input()
b = []
ast = []
for i in range(n):
    if s[i] == "|":
        b.append(i)
    elif s[i] == "*":
        ast = i
if b[0] < ast < b[1]:
    print("in")
else:
    print("out")
