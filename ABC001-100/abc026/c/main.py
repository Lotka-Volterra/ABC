n = int(input())
buka = [[] for i in range(n)]
for i in range(1, n):
    b = int(input())
    buka[b - 1].append(i)
salary = [0] * n
for i in range(n - 1, -1, -1):
    if len(buka[i]) == 0:
        salary[i] = 1
    else:
        buka_salary = []
        for j in buka[i]:
            buka_salary.append(salary[j])
        salary[i] = min(buka_salary) + max(buka_salary) + 1
print(salary[0])
