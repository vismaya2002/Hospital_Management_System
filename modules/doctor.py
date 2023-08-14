def InsertDoctor():
    name = input("Enter the name of doctor:  \n")
    age = int(input("Enter the age of doctor: \n"))
    dept = input("Enter the department of doctor: \n")
    qualific = input("Enter the qualification of the doctor: \n")
    phnnumber = int(input("enter the phone number of doctor: \n"))
    print("Patient created successfully")


def EditDoctor():
    while True:
        print("Edit The Details of Doctor...")
        id = int(input("enter the id of doctor: \n"))


def Doctor():
    while True:
        print("****** DOCTOR ******")
        print("1. Insert Details" )
        print("2. Edit Details" )
        print("3. Delete Details" )
        print("4. View Details" )
        print("5. Go Back" )
        x = int(input("Enter Your Choice : "))
        match x:
            case 1:
                InsertDoctor()

            case 2:
                EditDoctor()
                
            case 5:
                break