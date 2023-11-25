b = input()
code = ["A", "T", "G", "C"]
pair = ["T", "A", "C", "G"]
for i in range(4):
    if b == code[i]:
        print(pair[i])

#公式回答例
b = input()
c = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
print(c[b])