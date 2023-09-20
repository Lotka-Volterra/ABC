n = int(input())
s = []
flag = True
for i in range(n):
    s.append(input())
for i in range(n):
    if s[i][0] not in ["H", "D", "C", "S"]:
        flag = False
    if s[i][1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        flag = False
if len(list(set(s))) != n:
    flag = False
print(["No", "Yes"][flag])
