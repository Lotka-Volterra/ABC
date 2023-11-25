n, x = map(int, input().split())


def burger(currentBurger, layer):
    currentBurger = "B" + currentBurger + "P" + currentBurger + "B"
    layer += 1
    if layer == n:
        return currentBurger
    return burger(currentBurger, layer)


levelNBurger = burger("P", 0)
print(levelNBurger.count("P", 0, x))
