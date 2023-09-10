n = int(input())
s = input()

a = s.find("A")
b = s.find("B")
c = s.find("C")
print(max(a, b, c) + 1)
