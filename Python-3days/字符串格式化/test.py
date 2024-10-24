# 
# * hello world
name = "world"
print("Hello, %s!" % name)
    # * 使用"+"连接的字符串在输出时不会自动添加空格
print("Hello, " + name + "!")
    # * 使用","分隔的字符串在输出时会自动添加空格
print("Hello,", name, "!")

# * I love you
v = "love"
n = "you"
print("I %s %s" % (v, n))
print(f"I {v} {n}")
print("I {} {}".format(v, n))
print(f"I {v.upper()} {n.upper()}")

# * 1 + 1 = 2
num1 = 1
num2 = 1
print("%d + %d = %d" % (num1, num2, num1 + num2))
print(f"{num1} + {num2} = {num1 + num2}")
print("{} + {} = {}".format(num1, num2, num1 + num2))
print(f"{num1:02d} + {num2:02d} = {num1 + num2:02d}")
print(num1, "+", num2, "=", num1 + num2)
