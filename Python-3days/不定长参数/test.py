
# * 位置不定长 *args
def sum(*args):
    print(type(args), args)

sum(1, 2, 3, "你好")

# * 关键字不定长 **kwargs
def person(**kwargs):
    print(type(kwargs), kwargs)

person(name="张三", age=20, gender="男")
