
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
