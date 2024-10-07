
str = "万过薪月, 员序程马黑来, nohtyP学"
# * 倒序取出
print(str[10:4:-1])
# * 先倒序，再取出
print(str[::-1][10:15])
# * 先取出，再倒序
print(str[5:11][::-1])
# * 先分割，再替换
print(str.split(",")[1].replace("来", "")[::-1])
str = str.split(",")
str = str[1].replace("来", "")
str = str[::-1]
print(str)
