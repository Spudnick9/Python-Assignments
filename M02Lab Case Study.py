##Thomas Scherrer##
##This app will take an input of a student's first and ;ast name as well as their GPA and find out if it will fit into Honor Roll or Dean's List##
last_name = input("Please neter last name: ")
if last_name == "ZZZ":
    print("Quitting")
    

first_name = input("Please enter first name: ")
GPA = float(input("Please emter GPA: "))

if GPA >= 3.5:
    print("Student has made the Dean's List.")
elif GPA >= 3.25:
    print("Student has made Honor Roll.")