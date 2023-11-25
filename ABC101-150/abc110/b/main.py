n,m,x,y= map(int,input().split())
xi=list(map(int,input().split()))
yi=list(map(int,input().split()))
for i in range(x+1,y+1):
    if max(xi)<i<=min(yi):
        print('No War')
        quit()
print('War')