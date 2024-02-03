# import math

# x = int(input())
# year = 0
# while year < (math.log10(x) - 2) / math.log10(1.01):
#     year += 1
# print(year)
x = int(input())
money = 100
year = 0
while money < x:
    # 切り捨てなので、*1.01ではなく、*101//100
    money = money * 101 // 100
    year += 1
print(year)
