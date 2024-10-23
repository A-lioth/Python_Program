#
grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0}
sum1, sum2 = 0, 0
while True:
    grade = input()
    if grade == "False":
        break
    else:
        score = int(input())
        sum1 += grades[grade] * score
        sum2 += score
print("%.2f" % (sum1 / sum2))
