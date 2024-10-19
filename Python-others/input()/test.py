# 
# * input() 默认接收用户输入，并以字符串形式返回。

# * 1. 输入一个整数
num = int(input("请输入一个整数："))
print("你输入的整数是：", num)

# * 2. 输入多个使用空格分隔的整数
    # * 1. 使用map()函数
num1, num2 = map(int, input("请输入两个整数，用空格分隔：").split())
print("你输入的第一个整数是：", num1, "，第二个整数是：", num2)

    # * 2。使用列表解析
num1, num2 = [int(x) for x in input("请输入两个整数，用空格分隔：").split()]
print("你输入的第一个整数是：", num1, "，第二个整数是：", num2)

    # * 3. 使用列表
nums= input("请输入多个整数，用空格分隔：").split()
        # * 1. 使用列表解析
print("你输入的整数是：", [int(x) for x in nums])

        # * 2. 使用列表下标
print("你输入的第一个整数是：", nums[0], "，第二个整数是：", nums[1])

# * 3. 输入多个使用逗号分隔的字符串
    # * 1. 使用map()函数
name1, name2 = map(str, input("请输入两个名字，用逗号分隔：").split(","))
print("你输入的第一个名字是：", name1, "，第二个名字是：", name2)

    # * 2. 使用列表解析
name1, name2 = [x.strip() for x in input("请输入两个名字，用逗号分隔：").split(",")]
print("你输入的第一个名字是：", name1, "，第二个名字是：", name2)

    # * 3. 使用列表
name1, name2 = input("请输入两个名字，用逗号分隔：").split(",")
print("你输入的第一个名字是：", name1, "，第二个名字是：", name2)
