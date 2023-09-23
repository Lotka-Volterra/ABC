n= int(input())
w=[]
for i in range(n):
    w.append(input())
setw=[]
for i in range(n):
    if i<n-1:
        if w[i][-1]==w[i+1][0] and w[i] not in setw:
            setw.append(w[i])
        else:
            print('No')
            quit()
    elif w[i] in setw:
            print("No")
            quit()
print('Yes')