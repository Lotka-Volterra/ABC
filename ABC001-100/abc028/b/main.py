count=[0]*6
s=input()
for i in range(len(s)):
    count[ord(s[i])-ord("A")]+=1
print(*count)