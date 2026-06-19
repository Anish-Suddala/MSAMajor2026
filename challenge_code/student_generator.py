from Student import Student
def main():
    data_file = open("students.csv","r")
    print(data_file)
    students_list = []
    for line_of_data in data_file:
        student_info = line_of_data.split(",")
        print(line_of_data)
        s_fname = student_info[0]
        s_lname = student_info[1]
        s_major = student_info[2]
        s_chours = student_info[3]
        s_gpa = student_info[4]
        s_ID = student_info[5]





main()
