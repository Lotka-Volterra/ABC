l= int(input())
bunshi=1
bunbo=1
for i in range(1,12):
    bunshi*=(l-i)
    bunbo*=i
print(bunshi//bunbo)