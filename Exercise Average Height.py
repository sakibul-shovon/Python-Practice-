# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)   

total_height = 0;

for height in student_heights:
    total_height=total_height+height;

total_student = 0;

for student in student_heights:
    total_student = total_student + 1



average_height = round(total_height/total_student)

print(f"Average Height is {average_height}")