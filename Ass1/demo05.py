def calculate_grade(marks):

    average = sum(marks) / len(marks)            

    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"    
    elif 70 <= average < 80:
        grade = "C"
    elif 60 <= average < 70:
        grade = "D"
    else:
        grade = "F"

    return grade, average
    #    print(f"average = {average},marks = {marks},grade = {grade}")
marks = []
for subject in range(1, 4):
        mark = int(input(f"Enter marks for subjects {subject}: "))
        marks.append(mark)

average, grade = calculate_grade(marks)
    
print(f"Average = {grade}")
print(f"Grade = {average}")
#calculate_grade()

# def calculate_grade(marks):
#   """Calculates the average grade based on 3 marks (no validation)."""

#   # Assuming valid input (3 marks between 0-100)
#   average = sum(marks) / len(marks)

#   # Determine grade
#   if 90 <= average <= 100:
#     grade = "A"
#   elif 80 <= average < 90:
#     grade = "B"
#   elif 70 <= average < 80:
#     grade = "C"
#   elif 60 <= average < 70:
#     grade = "D"
#   else:
#     grade = "F"

#   return average, grade

# marks = []
# for subject in range(1, 4):
#   mark = int(input(f"Enter marks for subject {subject}: "))
#   marks.append(mark)

# average, grade = calculate_grade(marks)

# print(f"Average: {average:.2f}")
# print(f"Grade: {grade}")
