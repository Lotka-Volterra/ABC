abc = input()
a = abc[0]
b = abc[1]
c = abc[2]
print(int(a+b+c)+int(b+c+a)+int(c+a+b))
#公式回答　3文字で受け取る
a, b, c = input()
abc = a + b + c
bca = b + c + a
cab = c + a + b
ans = int(abc) + int(bca) + int(cab)
print(ans)
#abc の桁和である a+b+c を求め、これを 111 倍した値を出力する。
#(100a+10b+c)+(100b+10c+a)+(100c+10a+b)=111(a+b+c)より、
a,b,c=map(int,input())
print(111*(a+b+c))