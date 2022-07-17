n = int(input())

centdiv = n%100
if centdiv == 0:
    print(int(n/100))
else:
    print(n//100+1)