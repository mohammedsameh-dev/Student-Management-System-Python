import json
def log_operation(message):
        try:
                with open("log_file.txt","a") as f:
                        f.write(message + "\n")
                
        except Exception as e:
                print(f"Error saving log: {e}")
print("Hello And Welcome To My Student Management System")
while True:
        print("\nChoose One Of those Options: ")
        print(" 1. Add Student\n 2. View Students\n 3. Search for Student\n 4. Update Student\n 5. Delete Student\n 6. Exit")
        try:
                choice = int(input("What Do You Want To Choose: "))
                print("-----------########-----------")
                student = {}
                if   choice  == 1 :
                        try:
                                print("Please Enter\n* Student ID\n* Name\n* Age\n* Track")
                                student["id"]= int(input("ID: "))
                                student["name"]= input("Name: ")
                                student["age"]= int(input("Age: "))
                                student["track"]= input("Track: ")
                                try:
                                        with open("students.json","r") as f:
                                                x = json.load(f)
                                except FileNotFoundError:
                                                print("Error Finding the File")
                                                x["students"].append(student)
                                                with open("students.json", "w") as f:
                                                        json.dump(x, f, indent=4)
                                                        print("Student Added Successfully!")
                                                        log_operation(f"Added student {student['id']}")
                        except ValueError:
                                print("Error: Student ID and Age must be numbers!")
                        
                elif choice  == 2 :
                        with open("students.json") as f:
                                content = json.load(f)
                                print("\n--- Students List ---")
                                for i in range(len(content["students"])):
                                        print(content["students"][i])
                                        print("---------------------")
                        
                elif choice  == 3 :
                        isExist = False
                        number = -1
                        Uid = int(input("Please Enter a Student ID: "))
                        with open("students.json") as f:
                                Sid = json.load(f) 
                        for i in range(len(Sid["students"])):
                                if Uid == Sid["students"][i]["id"]:
                                        isExist = True
                                        number = i
                                        break
                        if isExist ==True:
                                print  (Sid["students"][number])
                                log_operation(f"Searched for student {Uid}")
                        else :
                                print  ("Sorry! This ID Doesn`t Exist")
                elif choice  == 4 :
                        isExist = False
                        number = -1
                        Uid = int(input("Please Enter a Student ID: "))
                        with open("students.json") as f:
                                Sid = json.load(f)
                        for i in range(len(Sid["students"])):
                                if Uid == Sid["students"][i]["id"]:
                                        isExist = True
                                        number = i
                                        break
                        if isExist ==True:
                                print  (f"Here the Old Information -> {Sid['students'][number]}\nto modify Enter The New Data")
                                student["id"]= int(input("Enter The New UserID: "))
                                student["name"]= input("Enter The New UserName: ")
                                student["age"]= int(input("Enter The New UserAge "))
                                student["track"]= input("Enter The New UserTrack: ")
                                Sid["students"][number] = student
                                with open("students.json", "w") as f:
                                        json.dump(Sid, f, indent=4)
                                print("Student Updated Successfully!")
                                log_operation(f"Updated student {Uid}")
                        else :
                                print  ("Sorry! This ID Doesn`t Exist")

                elif choice  == 5 :
                                isExist = False
                                number = -1
                                Uid = int(input("Please Enter a Student ID to delete: "))
                                with open("students.json") as f:
                                        Sid = json.load(f) 
                                for i in range(len(Sid["students"])):
                                        if Uid == Sid["students"][i]["id"]:
                                                isExist = True
                                                number = i
                                                break
                                if isExist ==True:
                                        deleted_student = Sid['students'][number]
                                        Sid['students'].pop(number)
                                        with open("students.json", "w") as f:
                                                json.dump(Sid, f, indent=4)
                                        print(f"Student With Data: {deleted_student} Has Been Deleted")
                                        log_operation(f"Deleted student {Uid}")
                                else :
                                        print  ("Sorry! This ID Doesn`t Exist")
                elif choice  == 6 :
                        print("The Application Has been Exited Bye Bye")
                        break
                else:
                        print("Enter A Valid Number Between 1 and 6")
        except ValueError:
                print("Error: Please enter a valid number for your choice.")
