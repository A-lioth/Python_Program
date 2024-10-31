#
# * {set} 无序
# survey_list = {"Niumei", "Niu Ke Le", "GURR", "LOLO"}
# * [list] 有序
survey_list = ["Niumei", "Niu Ke Le", "GURR", "LOLO"]

result_dict = {"Niumei": "Nowcoder", "GURR": "HUAWEI"}

[
    print
    (
        "Hi, " + name + "! Thank you for participating in our graduation survey!"
        if result_dict.get(name)
        else "Hi, " + name + "! Could you take part in our graduation survey?"
    )
    for name in survey_list
]
