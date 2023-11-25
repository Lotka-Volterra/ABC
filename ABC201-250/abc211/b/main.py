s=[]
for i in range(4):
    s.append(input())
print("Yes") if len(list(set(s)))==4 else print("No")