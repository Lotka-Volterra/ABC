n= int(input())
k=0
for i in range(19):
    if 2**k<n<2**(k+1):
        print(k)
        quit()
    k+=1
