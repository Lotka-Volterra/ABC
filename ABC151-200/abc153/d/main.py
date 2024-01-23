h = int(input())
number = 1
count = 0
while h > 0:
    count += number
    h //= 2
    number *= 2
print(count)
