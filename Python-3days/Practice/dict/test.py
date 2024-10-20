# 
employees = {
    "wang": {
        "部门": "科技",
        "工资": 3000,
        "级别": 1
        },
    "zhou": {
        "部门": "市场",
        "工资": 5000, 
        "级别": 2
        },
    "lin": {
        "部门": "市场", 
        "工资": 7000, 
        "级别": 3
        },
    "zhang": {
        "部门": "科技",
        "工资": 4000, 
        "级别": 1
        },
    "liu": {
        "部门": "市场",
        "工资": 6000, 
        "级别": 2
        }
}
print(employees)

for name in employees:
    if employees[name]["级别"] == 1:
        employees[name]["工资"] += 1000
        employees[name]["级别"] += 1
    elif employees[name]["级别"] == 2:
        employees[name]["工资"] += 2500
    elif employees[name]["级别"] == 3:
        employees[name]["部门"] = "管理"

print(employees)

# * get()
print(employees.get("wang"))
print(employees["wang"].get("部门"))
print(employees.get("li", "不存在"))
print(employees["wang"].get("职位", "不存在"))
