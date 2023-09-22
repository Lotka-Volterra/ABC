a, b = map(int, input().split())
tap = 1
for i in range(21):
    if tap >= b:
        print(i)
        quit()
    tap += a - 1
