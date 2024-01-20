n = int(input())
num_check = [0] * (2 * n + 2)
num_check[0] = 1
for i in range(n + 1):
    for j in range(1, 2 * n + 2):
        if num_check[j] == 0:
            print(j)
            num_check[j] = 1
            break
    aoki = int(input())
    num_check[aoki] = 1
