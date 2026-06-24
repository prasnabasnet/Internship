

print("=== Student Marks System ===\n")


num_subjects = int(input("Enter number of subjects: "))


students = {}
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ").strip()
    print(f"Enter {num_subjects} subject's marks for {name} (space separated):")
    marks = list(map(int, input().split()))
    
    
    if len(marks) != num_subjects:
        print(f"Warning: Expected {num_subjects} marks, got {len(marks)}")
    
    students[name] = marks


print("          STUDENT MARKS REPORT")

total_class_avg = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks) if marks else 0
    total_class_avg += avg
    
    
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{name:20} | Marks: {marks} | Avg: {avg:.2f} | Grade: {grade}")


class_average = total_class_avg / n if n > 0 else 0
print(f"CLASS TOTAL AVERAGE : {class_average:.2f}")