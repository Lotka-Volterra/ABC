x = input()
if int(x) % 1111 == 0:
    print("Weak")
    quit()
for i in range(1, 4):
    if (int(x[i - 1]) + 1) % 10 != int(x[i]):
        print("Strong")
        quit()
print("Weak")
