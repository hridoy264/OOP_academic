
student_records = {}

while True:
    name = input("Enter student name: ")
    cgpa = float(input("Enter CGPA: "))
    
    student_records[name] = cgpa
    
    choice = input("Do you want to Enter another record Press 'y' if yes : ")
    print() 
    
    if choice.lower() != 'y':
        break


print(student_records)