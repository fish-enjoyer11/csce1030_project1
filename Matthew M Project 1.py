student_ids = [1001, 1002, 1003, 1004]                                       #create a list of student names, brackets are list
student_names = ["Alex Mercer", "Jordan Lee", "Ivo Robotnik", "Lucy Luanne"] #same for student names, its a list
enrolled_courses = set(["CS101", "MATH201", "ENG102"])

student_grades = { #create a dictionary which maps student id to grades
    1001:[88.5, 92.0, 79.0, 95.5],
    1002:[89.0, 92.5, 95.5, 93.0],
    1003:[72.0, 85.0, 92.5, 98.5],
    1004:[86.5, 80.0, 81.5, 83.5]
}
student_gpas = { #default values for gpa, option 2 needs to be able to update them?
    1001:3.0,
    1002:4.0,
    1003:3.0,
    1004:3.0,
}
GRADE_BOUNDARIES = tuple([90.0, 80.0, 70.0, 60.0]) #create tuple for grade boundaries, i hope i did this right
GRADE_LETTERS = tuple(["A", "B", "C", "D", "F"]) #tuple for letter grades

application_isactive = True #Set to true by default or else the program doesn't run :P


while application_isactive == True: #remember to use continue to skip the rest of the code in an iteration
    #heres where the magic happens baby
    print("\nMENU:\n\n1. View All Student Records\n\n2. Add New Student Record\n\n3. Search & Update Student Grades\n")
    print("4. View Class Analytics & Summary\n\n5. Exit System\n")
    user_input = int(input("Select an option (1-5): "))

    if(user_input == 5):              #this is our input check. start by checking if its the exit command.
        application_isactive = False
    elif(user_input in range(1,5)):   #this actually checks if its 1 through 4. The 5 at the end is exclusive.
        print("Successfully triggered a menu option")

        if(user_input == 2): #BEGIN OPTION 2: Add a new Student Record

            print("\n----Add New Student Record----\n")

            new_id = input("Input a student ID (4 numbers): ") #prompt user for new id input

            if new_id.isdigit() and (len(new_id) == 4): #if the user has input a valid id format

                print(new_id, "is valid")

                new_name = input("Enter student's full name: ")
                new_course = input("Enter enrolled course: ")

                enrolled_courses.add(new_course.upper())
                print(enrolled_courses)


                if(int(new_id) not in student_ids): #check if the newly input id already exists
                    print(f"{new_id} not present in list.")
                else:
                    print(f"{new_id} present in list.")
                

            else:
                print(f"ERROR: {new_id} not a valid ID")


    else:
        print(f"ERROR: {user_input} is not a valid input.")


#if we get here, presumably we have broken the while loop
print("\nApplication Exited Successfully(?)")