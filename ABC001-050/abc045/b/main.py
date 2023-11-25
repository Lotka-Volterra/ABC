# personは誰のターンか
def saiki(person):
    personlist = "ABC"
    personnumber = 0
    # personがaでなければ更新
    if person == "b":
        personnumber = 1
    elif person == "c":
        personnumber = 2

    if len(slist[personnumber]) == 0:
        # その人のターンかつ、カードを持ってなかったらその人の勝ち
        print(personlist[personnumber])
        quit()
    else:
        nextperson = slist[personnumber][0]
        if len(slist[personnumber]) > 1:
            slist[personnumber] = slist[personnumber][1:]
        else:
            slist[personnumber] = ""
        # 次の人のターン（再帰関数を呼ぶ）
        saiki(nextperson)


slist = []
for i in range(3):
    slist.append(input())
saiki("a")
