from itertools import combinations


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def is_square(A, B, C, D):
    points = [A, B, C, D]
    distances = set()

    for pair in combinations(points, 2):
        distances.add(distance(pair[0], pair[1]))

    if len(distances) != 2:
        return False

    diagonal = max(distances)
    distances.remove(diagonal)

    side = distances.pop()

    for point in points:
        if distance(point, ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)) != side:
            return False

    return True


s = []
for i in range(9):
    s.append(input())
point = []
for i in range(9):
    for j in range(9):
        if s[i][j] == "#":
            point.append((i, j))
ans = 0
for i in range(len(point) - 3):
    for j in range(i + 1, len(point) - 2):
        for k in range(j + 1, len(point) - 1):
            for l in range(k + 1, len(point)):
                print(i, j, k, l)
                print(point)
                if is_square(point[i], point[j], point[k], point[l]):
                    ans += 1
print(ans)
