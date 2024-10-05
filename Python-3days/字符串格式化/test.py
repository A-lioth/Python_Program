
# * hello world
name = "world"
print("Hello, %s!" % name)

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
