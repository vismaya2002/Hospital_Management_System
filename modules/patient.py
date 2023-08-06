def InsertPatient():
    name = input("Enter the name of patient : \n")
    age = int(input("Enter the age of patient : \n"))
    PhnNumber = int(input("Enter the phone number of patient : \n"))
    ConsultingDepartment = input("Enter the department consulted : \n")
    ConsulitngDoctor = input("Enter the name of doctor consulting : \n")

def NameEdit(id):
    NewName = input("Enter the corrected name of patient: ")

def AgeEdit(id):
    NewAge = input("Enter the corrected age of patient: ")

def PhoneNumberEdit(id):
    NewNumber = int(input("Enter the corrected age of patient: "))


def EditPatient():
    while True:

        print("Edit The Details Of Patient...")
        id = input("Enter the PatientId: \n")
        print("1. Edit Patient Name")
        print("2. Edit Patient age")
        print("3. Edit Patient Phone Number")
        print("4. Edit Consulting Department")
        print("5. Edit Consulting Doctor")
        print("6. Go Back")
        y = int(input("Enter Your Choice: "))
        match y:
            case 1:
                NameEdit(id)
            case 2:
                AgeEdit(id)
            case 3:
                PhoneNumberEdit(id)
            case 6:
                break
            case _:
                print("You Entered The Wrong Choice.")



                

def Patient():
    while True:

        print("******* PATIENT *******")
        print("1. Insert Details")
        print("2. Edit Details")
        print("3. Delete Details")
        print("4. View Details")
        print("5. Go Back")
        x = int(input("Enter Your Choice : "))
        match x:
            case 1:
                InsertPatient()

            case 2:
                EditPatient()
                
            case 5:
                break



    