n = int(input())
s = []
t = []
for i in range(n):
    si, ti = input().split()
    s.append(si)
    t.append(ti)
for i in range(n):
    for j in range(i+1,n):
        if s[i]==s[j] and t[i]==t[j]:
            print('Yes')
            quit()
print('No')

#s,tをまとめて考える。「整数対 (i,j)) が存在する」とは、「重複がある」ということで、
#setに変換してサイズがN未満かどうかで判定できる。
N = int(input())
ST = [input() for _ in range(N)]

print("Yes" if len(set(ST))<N else "No")
