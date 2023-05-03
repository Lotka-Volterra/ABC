s = input()
t = input()
lens = len(s)
s2 = s + s
for i in range(lens):
    slices2 = s2[i:i+lens]
    if slices2 == t:
        print("Yes")
        quit()
print("No")
