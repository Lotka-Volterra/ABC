S,T = input().split()
A,B = map(int,input().split())
U = input()
a = str(A-1)
b = str(B-1)
if U == S:
    print(a+" "+str(B))
else:
    print(str(A)+" "+b)

#数字(int)を空白区切りで出力するには、カンマ
print(A,b) #A b
