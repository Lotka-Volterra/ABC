a, b = input().split()
int_a = int(a)
# print(b[:-3])
int_b = int(b[:-3]) * 100 + int(b[-2:])
print(int_a * int_b // 100)
