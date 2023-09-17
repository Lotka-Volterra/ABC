n= int(input())
hh=n//3600
n=n-3600*hh
mm=n//60
n=n-60*mm
ss=n
ans=''
time=[hh,mm,ss]

if hh>=24:
    print('23:59:59')
else:
    for i in range(3):
        if len(str(time[i]))==1:
            time[i]='0'+str(time[i])
        else:
            time[i]=str(time[i])
print(time[0]+':'+time[1]+':'+time[2])
