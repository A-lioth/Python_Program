#
current_users = ["Niuniu", "Niumei", "GURR", "LOLO"]
new_users = ["GurR", "Niu Ke Le", "LoLo", "Tuo Rui Chi"]
# * 1 双重循环
for i in new_users:
    for j in current_users:
        if i.lower() == j.lower():
            print(
                "The user name",
                i,
                "has already been registered! Please change it and try again!",
            )
            break
    else:
        print("Congratulations, the user name", i, "is available!")

# * 2 if...in.../map()/lambda/list()
for c in new_users:
    if c.upper() not in list(map(lambda x: x.upper(), current_users)):
        print("Congratulations, the user name", c, "is available!")
    else:
        print("The user name", c, "has already been registered! Please change it and try again!")
