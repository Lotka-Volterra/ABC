x = input()
n = int(input())
name = []

order = [0] * 26
for i in range(26):
    order[ord(x[i]) - ord("a")] = i
for i in range(n):
    s = input()
    renamed = ""
    for j in s:
        renamed += chr(order[ord(j) - ord("a")] + ord("a"))
    name.append([renamed, s])
name.sort()
for i in range(n):
    print(name[i][1])
