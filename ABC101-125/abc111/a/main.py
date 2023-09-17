n = input()
N = ""
for i in range(3):
    if n[i] == "1":
        N += "9"
    else:
        N += "1"
print(N)

#数字の置き換えは、以下のようにもできる
for i in range(3):
    N+=str(9+1-int(n[i]))
#これを利用すると、
n= int(input())
print(999+111-n)


#別解　別の文字を経由して文字の置き換え
n = input()
n = n.replace('1','x')
n = n.replace('9','1')
n = n.replace('x','9')
print(n)