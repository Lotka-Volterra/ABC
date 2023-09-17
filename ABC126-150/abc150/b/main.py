n= int(input())
s=input()
count=0
for i in range(n-2):
    if s[i:i+3]=="ABC":
        count+=1
        i+=3
print(count)

#別解 ただしこれは、部分文字列の区別ができない。（今回は同じ文字が複数のABCに含まれることはないので問題ない）
#print('ABABA'.count'('ABA'))
#は１が出力される。count()は重複せず出現する回数を数えるので、print('ABAABA'.count('ABA'))は２が出力
print(s.count('ABC'))