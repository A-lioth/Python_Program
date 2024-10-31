# 
# * 比大小
    # * 两个数
# a, b = map(int, input().split())
# max = a if a > b else b
# min = a if a < b else b
# print(max, min)
    # * 多个数
# a, b, c = map(int, input().split())
# max = a if a> b else (b if b > c else c)
# min = a if a < b else (b if b < c else c)
# print(max, min)

# * 输出字符串
name = ['alice', 'bob', 'tom']
    # * 每行输出一个字符串
boss = ['tim', 'tom']
[
    print
    (
        '我是' + i 
        if i in boss 
        else '我不是' + i
    ) 
    for i in name
]
    # * 一行输出所有字符串
print
(
    [
        '我是' + i 
        if i in boss 
        else '我不是' + i 
        for i in name
    ]
)
