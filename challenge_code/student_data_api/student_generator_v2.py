from Student import Student
def main():
    data_file = open("students.csv","r")
    students_list = []
    line_number = 0
    for line_of_data in data_file:
        line_number+=1
        if line_number == 1:
            continue
        student_info = line_of_data.split(",")
        print(line_of_data)
        if(len(student_info)!=6):
            print("ERROR: Invalid Format")
            continue    
        s_fname = student_info[0]
        s_lname = student_info[1]
        s_major = student_info[2]
        s_chours = student_info[3]
        s_gpa = student_info[4]
        s_ID = student_info[5]
        
        try:
            student: Student = Student(s_fname, s_lname, s_major, int(s_chours), float(s_gpa), s_ID.strip())
        except:
            print("Error: INVALID FORMATTING")
            continue
        s_Level = student.get_class_level()
        students_list.append(student)
    data_file.close()
    for student in students_list:
        print(f"{student.get_first_name()} {student.get_last_name()} ")
        print(f"Class Level: {s_Level}, Major: {student.get_major()}")
        print(f"GPA: {student.get_gpa()}, ID: {student.get_ID()}")







main()
