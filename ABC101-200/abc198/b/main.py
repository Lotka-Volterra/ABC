n = int(input())
for i in range(1, len(str(n))):
    if n % 10 != 0:
        break
    n //= 10
n = str(n)
for i in range(len(n)):
    if n[i] != n[-i - 1]:
        print("No")
        quit()
print("Yes")
