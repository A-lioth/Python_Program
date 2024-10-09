
# * 常规异常
try:
    a = 10 / 0
    print(a)
except:
    print("出现异常")

# * 自定义异常
try:
    print(a)
except NameError:
    print("变量 a 未定义")
# except NameError as e:
#     print(e)
try:
    print(1 / 0)
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("ZeroDivisionError or NameError")
    print(e)

# * 所有异常
try:
    print(1 / 0)
    print(name)
except Exception as e:
    print("出现异常")
    print(e)
else:
    print("没有异常")
finally:
    print("程序结束")
