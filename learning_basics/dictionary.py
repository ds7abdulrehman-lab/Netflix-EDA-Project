student = {"name": "Ali", "marks": [85, 92, 78]}

# 1️⃣ Add a new key "age" with the value 23
# 2️⃣ Calculate the average of the marks
# 3️⃣ Print the updated dictionary and the average

student["age"] = 23


mark =student["marks"]
average_marks = sum(mark)/len(mark)
    


print(student)
print(average_marks)