n= int(input())
s=input()
mae=s[0]
count=1
for i in range(1,n):
    if s[i]!=mae:
        count+=1
        mae=s[i]
print(count)