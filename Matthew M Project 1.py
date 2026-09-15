student_ids = [1001, 1002, 1003, 1004]                                       #create a list of student names, brackets are list
student_names = ["Alex Mercer", "Jordan Lee", "Ivo Robotnik", "Lucy Luanne"] #same for student names, its a list
enrolled_courses = set(["CS101", "MATH201", "ENG102"])

student_grades = { #create a dictionary which maps student id to grades
    1001:[88.5, 92.0, 79.0, 95.5],
    1002:[89.0, 92.5, 95.5, 93.0],
    1003:[72.0, 85.0, 92.5, 98.5],
    1004:[86.5, 80.0, 81.5, 83.5]
}
student_gpas = { #default values for gpa, option 2 needs to be able to update these
    1001:3.0,
    1002:4.0,
    1003:3.0,
    1004:3.0,
}
GRADE_BOUNDARIES = tuple([90.0, 80.0, 70.0, 60.0]) #create tuple for grade boundaries, i hope i did this right
WEIGHTED_GPAS = tuple([4.0, 3.0, 2.0, 1.0])          #tuple for gpas on a 4.0 scale
GRADE_LETTERS = tuple(["A", "B", "C", "D"]) #tuple for letter grades

application_isactive = True #Set to true by default or else the program doesn't run :P


while application_isactive == True: 
                            #this loop will repeat forever until the user inputs 0 at the main menu.
                            #please remember that indentation matters A LOT for making sure our code works together with each other
                            #also, use hashtags to start a comment. they dont affect the program but leaving them for each other
                            #will make all of our lives so much easier.
    
    print("\nMENU:\n\n1. Add New Student Record\n\n2. Compute GPAs & Academic Averages\n\n3. Display Grade Roster\n")
    print("4. Search for Student & Flag Academic Risk\n\n5. Class Statistics\n")
    user_input = int(input("Select an option (1-5), 0 to exit: "))

    if(user_input == 0):              #this is our input check. start by checking if its the exit command.
        application_isactive = False
    elif(user_input in range(1,6)):   #this actually checks if its 1 through 5. The 6 at the end is exclusive.

        print("Successfully triggered a menu option") #this is just a debug message to make sure the menu works

        if(user_input == 1): #BEGIN OPTION 1: Add a new Student Record

            print("\n----Add New Student Record----\n")

            new_id = input("Input a student ID (4 numbers): ") #prompt user for new id input

            if new_id.isdigit() and (len(new_id) == 4): #if the user has input a valid id format

                new_id = int(new_id)
                print(new_id, "is valid")

                new_name = input("Enter student's full name: ")
                new_course = input("Enter enrolled course: ")

                try:
                    num_scores_to_add = int( input("How many scores will be added? ") )
                except ValueError:
                    print("ERROR: input must be convertible to integer.")
                    input()
                    continue

                i = 1                   #use this to increment once each iteration until i = num_scores_to_add
                new_grade_list = list() #list to hold each new grade entered

                while i <= int(num_scores_to_add):
                    try:
                        new_grade_list.append(float( input(f"Enter score number {i}: ") ) ) #add each new entered grade to the end of the list
                        i += 1 #increment i by 1 for each successful iteration so we arent in an endless loop
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
                    input() #we can use input() on its own as a sort of "pause button" to make the program wait for input before continuing
                            #do that if you feel like the user needs to see whats going on before the program continues.

                else: #if id already exists, replace name and grades with input
                    print(f"{new_id} present in list. No changes will be made.")
                    #student_names[student_ids.index(new_id)] = new_name
                    #student_grades[new_id] = new_grade_list
                    #debug statements
                    print("List of students:", student_names)
                    print("Grades for", new_id, "are", student_grades[new_id])
                    input()
                

            else:
                print(f"ERROR: {new_id} not a valid ID")

        if(user_input == 2): #BEGIN OPTION 2: Compute GPAs & Academic averages

            if student_grades: #by using student_grades as the if-check, it returns True if the dict contains items. If its empty, returns False

                student_lettergrades = dict() #temporarily create empty dictionary to hold ID-lettergrade pairs
                
                for stud_id in student_grades:

                    gpa_avg = sum(student_grades[stud_id]) / len(student_grades[stud_id]) #calculate gpa in average form

                    for (i, cutoff) in enumerate(GRADE_BOUNDARIES): #i need to study this more
                        if(gpa_avg >= cutoff): #example: if gpa_avg = 91 then 91 >= 90, student grade is 4.0 - 0 = 4.0
                            student_gpas[stud_id] = (4.0 - i)
                            student_lettergrades[stud_id] = GRADE_LETTERS[i] #this should get "A" for 0, "B" for 1, etc.
                            break #break this for loop, or else it will eventually fail and produce an "F"
                        else:
                            student_gpas[stud_id] = (0.0)
                            student_lettergrades[stud_id] = "F" #start work from here later




                print(student_gpas)
                print(student_lettergrades)
                input()
            else: #since the program is initialized with grades, this should never happen
                print("Student grades is empty.") 
                input()

    else:
        print(f"ERROR: {user_input} is not a valid input.")


#if we get here, presumably we have broken the while loop
print("\nApplication Exited Successfully(?)")