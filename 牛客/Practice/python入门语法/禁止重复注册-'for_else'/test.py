#
current_users = ["Niuniu", "Niumei", "GURR", "LOLO"]
new_users = ["GurR", "Niu Ke Le", "LoLo", "Tuo Rui Chi"]
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
