#Christina
#Homework To do list

#functions
while True:
    print("Welcome to the To Do List App!")
    print("""
        1.Add an item to the to-do list
        2. Mark an item as Done
        3. Remove an item or Clear the List
        4. Exit the program""")
    list=input("What would you like to do today?: ")

    homework=["French Homework", "HUSH Homework","AP ComSci Homework","Math Homework","English Homework","Drivers Ed Homework","Chemistry Homework"]
    finished_homework=[]
    if list=="1":
        adding=input("What is the name of the homework you would like to add?: ")
        homework.append(adding)
        print(homework)
        continue

    elif list=="2":
        done=input("What homework are you finished with?: ")
        try:
            homework.remove(done)
        except:
            print("An error occured, please try again!")

        finished_homework.append(done)
        print("To Do: ")
        print(homework)
        print("Finished Homework: ")
        print(finished_homework)
        continue

    elif list=="3":
        unwanted=input("What homework would you like to remove?: ")
        try:
            homework.remove(unwanted)
        except:
            print("An error occured, please try again!")
        print("To Do: ")
        print(homework)
        print("Finished Homework: ")
        print(finished_homework)

        continue

    elif list=="4":
        print("Goodbye!")
        break

