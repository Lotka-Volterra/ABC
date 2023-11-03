s = input()
wb = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"

if s == wb[0:20] or s == wb[1:21]:
    print("Do")
elif s == wb[2:22] or s == wb[3:23]:
    print("Re")
elif s == wb[4:24]:
    print("Mi")
elif s == wb[5:25] or s == wb[6:26]:
    print("Fa")
elif s == wb[7:27] or s == wb[8:28]:
    print("So")
elif s == wb[9:29] or s == wb[10:30]:
    print("La")
else:
    print("Si")
