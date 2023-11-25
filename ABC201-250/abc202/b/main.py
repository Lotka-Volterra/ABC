org_str = input()

new_str_list = list(reversed(org_str))

new_str = "".join(list(reversed(org_str)))
r_str = new_str.replace("6", "X").replace("9", "6").replace("X", "9")
print(r_str)
