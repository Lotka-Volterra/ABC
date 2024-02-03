AB = list(map(int, input().split()))

for i in range(2):
    if AB[i] == 1:
        AB[i] += 13
if AB[0] > AB[1]:
    print("Alice")
elif AB[0] == AB[1]:
    print("Draw")
else:
    print("Bob")
