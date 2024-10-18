#

# * join()

# * 1
num = [1, 2, 3, 4, 5]
print("".join(str(i) for i in num))

# * 2
chars = ["a", "b", "c", "d", "e"]

# *使用无分割符连接
print("".join(chars))

# *使用空格分割符连接
print(" ".join(chars))

# *使用逗号分割符连接
print(",".join(chars))


num = input()
# * 1
for i in (2, 3, 0, 1):
    print("".join(str((int(num[i]) + 3) % 9)), end="")
# * 2
print("".join(str((int(num[i]) + 3) % 9) for i in (2, 3, 0, 1)))
