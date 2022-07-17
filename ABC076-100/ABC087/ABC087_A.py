x = int(input())
a = int(input())
b = int(input())
x -= a
c = x//b
print(x-b*c)

# 余りを求めるので、以下で良い
print((x-a) % b)
