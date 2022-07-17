a,b= map(int,input().split())
print(max(a+b,2*a-1,2*b-1))
#大きいボタンを2回押すのが最適。ただし、a=bなら、異なるボタンを1回ずつ押すのが最適。
a,b= map(int,input().split())
if a!=b:
    print(2*max(a,b)-1)
elif a==b:
    print(2*a)