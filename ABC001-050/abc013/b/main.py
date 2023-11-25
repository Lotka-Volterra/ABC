a = int(input())
b = int(input())

if a>b:
    print(min(a-b,b+10-a))
else:
    print(min(b-a,a+10-b)) 

#別解
print(min(abs(a-b),10-abs(a-b)))