#以下のコードは、７以外が末尾になると７を含んでいてもNoを返すので駄目
n = input()
result = 0
for i in n:
    if i == "7":
        result = 'Yes'
    else:
        result = 'No'

print(result)

n = int(input())

total = 0
for i in range(n+1):
    if i % 3 != 0 and i % 5 !=0:
        total += i
print(total)