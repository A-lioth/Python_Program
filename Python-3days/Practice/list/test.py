
students_age = [21, 25, 21, 23, 22, 20]
students_age.append(31)
new_students_age = [29,33,30]
students_age.extend(new_students_age)
print(students_age[0])
print(students_age[-1])
print(students_age.index(31))
for age in students_age:
    print(age)
