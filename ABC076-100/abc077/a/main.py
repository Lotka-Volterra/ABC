s1=input()
s2=input()
judge="YES"
if s1[0]!=s2[2]:
    judge="NO"
elif s1[1]!=s2[1]:
    judge="NO"
elif s1[2]!=s2[0]:
    judge="NO"

print(judge)

#まとめて
if s1[0]!=s2[2] or s1[1]!=s2[1] or s1[2]!=s2[0]:
    print("NO")
else:
    print("YES")