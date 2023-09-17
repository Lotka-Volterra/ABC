x =int(input())
happiness = 0
s500 = x//500
s5 = (x-500*s500)//5
happiness = s500*1000 + s5*5
print(happiness)