# * list = [推导语句 for i in list] ，可以省略append和创建空list这两个步骤。

# * 1 创建列表元素
# list = list()
# for i in range(1, 10):
#     list.append(i)
# print(list)

# list = [i for i in range(1, 10)]
# print(list)

# * 2 修改列表元素
# list_1 = [0, 1, 2, 3, 4]
# list_2 = list()
# for i in list_1:
#     i += 1
#     list_2.append(i)
# print(list_2)

# list_1 = [0, 1, 2, 3, 4]
# list_2 = [i+1 for i in list_1]
# print(list_2)

# * 输出
result_dict = {
    "Allen": ["red", "blue", "yellow"],
    "Tom": ["green", "white", "blue"],
    "Andy": ["black", "pink"],
}
# * 每行输出一个元素
# [print(i) for i in range(1, 10)]
    # * 双层列表推导式
# [
#     print(name, "'s favorite colors are: ", sep = "") or print(color)
#     for name in sorted(result_dict)
#     for color in result_dict.get(name)
# ]
# [
#     print(name, "'s favorite colors are: ", sep = "")
#     or [print(color) for color in result_dict.get(name)]
#     for name in sorted(result_dict)
# ]
# * 一行输出所有元素
# print([i for i in range(1, 10)])
