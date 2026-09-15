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

        if(user_input == 1): #Start here next, OPTION 1: VIEW ALL STUDENT RECORDS 
            pass

        if(user_input == 2): #BEGIN OPTION 2: Add a new Student Record

            print("\n----Add New Student Record----\n")

            new_id = input("Input a student ID (4 numbers): ") #prompt user for new id input

            if new_id.isdigit() and (len(new_id) == 4): #if the user has input a valid id format

                new_id = int(new_id)
                print(new_id, "is valid")

                new_name = input("Enter student's full name: ")
                new_course = input("Enter enrolled course: ")

                num_scores_to_add = int( input("How many scores will be added? ") )

                i = 1                   #use this to increment once each iteration until i = num_scores_to_add
                new_grade_list = list() #list to hold each new grade entered

                while i <= num_scores_to_add:
                    try:
                        new_grade_list.append(float( input(f"Enter score number {i}: ") ) ) #add each new entered grade to the end of the list
                        i += 1 #increment i by 1 so we arent in a hell cycle
                    except ValueError:
                        print("Error: input type not accepted (floats only please)")
                        continue

                enrolled_courses.add(new_course.upper()) #add course to enrolled_courses set



                if(new_id not in student_ids): #check if the newly input id already exists
                    print(f"{new_id} was not present, now adding.")
                    student_ids.append(new_id)
                    student_names.append(new_name)
                    student_grades[new_id] = new_grade_list
                    #debug statements
                    print("New ID:", new_id)
                    print("List of students:", student_names)
                    print("Grades for", new_id, "are", student_grades[new_id])

                else: #if id already exists, replace name and grades with input
                    print(f"{new_id} present in list. Updating Entry.")
                    student_names[student_ids.index(new_id)] = new_name
                    student_grades[new_id] = new_grade_list
                    #debug statements
                    print(student_names)
                    print("Grades for", new_id, "are", student_grades[new_id])
                

            else:
                print(f"ERROR: {new_id} not a valid ID")


    else:
        print(f"ERROR: {user_input} is not a valid input.")


#if we get here, presumably we have broken the while loop
print("\nApplication Exited Successfully(?)")