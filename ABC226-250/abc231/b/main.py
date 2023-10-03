n = int(input())
dict = {}
for i in range(n):
    s = input()
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1
candidate = []
for key, value in dict.items():
    candidate.append([value, key])
candidate.sort(reverse=True)
print(candidate[0][1])
