from itertools import permutations


def distance(p1, p2):
    return (x_y[p1][0] - x_y[p2][0]) ** 2 + (x_y[p1][1] - x_y[p2][1]) ** 2


n = int(input())
x_y = []
for i in range(n):
    x, y = map(int, input().split())
    x_y.append([x, y])
towns = list(range(n))
sum = 0
per_list = list(permutations(towns))
for pair in per_list:
    for i in range(n - 1):
        a = (distance(pair[i], pair[i + 1])) ** (1 / 2)
        sum += a
print(sum / len(per_list))
