# 
# * 比大小
    # * 两个数
a, b = map(int, input().split())
max = a if a > b else b
min = a if a < b else b
print(max, min)
    # * 多个数
a, b, c = map(int, input().split())
max = a if a> b else (b if b > c else c)
min = a if a < b else (b if b < c else c)
print(max, min)
