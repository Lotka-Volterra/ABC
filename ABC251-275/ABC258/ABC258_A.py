k= int(input())
if k<=9:
    kk='0'+str(k)
    print('21:'+kk)
elif k<=59:
    print('21:'+str(k))
elif k <=69:
    kk='0'+str(k-60)
    print('22:'+str(kk))
else:
    kk=k-60
    print('22:'+str(kk))