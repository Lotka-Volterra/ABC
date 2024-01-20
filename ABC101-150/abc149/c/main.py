def is_prime(integer):
    prime = True
    for i in range(2, integer):
        if i**2 > integer:
            break
        if integer % i == 0:
            prime = False
            break
    return prime


x = int(input())
ans = 100003
for i in range(x, ans):
    if is_prime(i):
        print(i)
        quit()
print(ans)
