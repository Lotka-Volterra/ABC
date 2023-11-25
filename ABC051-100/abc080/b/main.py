n = input()
fn = 0
for i in range(len(n)):
    fn += int(n[i])
if int(n) % fn == 0:
    print("Yes")
else:
    print("No")
