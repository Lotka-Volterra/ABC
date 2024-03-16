k = int(input())
amari = 7 % k
if amari == 0:
    print(1)
    quit()
for i in range(1, k):
    amari = (10 * amari + 7) % k
    if amari == 0:
        print(i + 1)
        quit()
print(-1)
