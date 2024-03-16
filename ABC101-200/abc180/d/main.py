x, y, a, b = map(int, input().split())
x_b = x
experience = 0
while a * x <= y:
    x *= a
    experience += 1
y_ab = y - x
experience += y_ab // b
y_b = y - x_b
experience_b = y_b // b
print(max(experience, experience_b))
