s=input()
ordA=ord('A')
ans=0

for i in range(len(s)):
    slicedS=s[-(i+1)]
    ordSlicedS=ord(slicedS)-ordA+1
    ans+=ordSlicedS*26**i
print(ans)