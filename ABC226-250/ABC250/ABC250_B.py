n,a,b= map(int,input().split())
for i in range(1,a*n+1):
    s=""
    for j in range(1,b*n+1):
        if (1<=i %(2*a)<=a):
            if (1<=j%(2*b)<=b):
                s+="."
            else:
                s+="#"
        else:
            if (1<=j%(2*b)<=b):
                s+="#"
            else:
                s+="."
    print(s)
