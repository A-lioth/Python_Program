
colors = ['red', 'green', 'blue', 'yellow']
print(colors)
print(colors[-1])
print(colors[1:3])
print(colors.index('green'))
colors[0] = "black"
print(colors[0])
colors.insert(2, "white")
print(colors)
colors.remove("yellow")
print(colors)
colors.pop(1)
print(colors)

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([nums[0][1], nums[1][1], nums[2][1]])
print(nums.index([4, 5, 6]))
