def InsertPatient(connection,cursor):
    cursor.execute('select * from patient')
    val = cursor.fetchall()
    id = len(val)+101
    name = input("Enter the name of patient : \n")
    age = int(input("Enter the age of patient : \n"))
    PhnNumber = int(input("Enter the phone number of patient : \n"))
    ConsultingDepartment = input("Enter the department consulted : \n")
    ConsulitngDoctor = input("Enter the name of doctor consulting : \n")
    cursor.execute("insert into patient values({},'{}',{},{},'{}','{}')".format(id,name,age,PhnNumber,ConsultingDepartment,ConsulitngDoctor))
    connection.commit()
    print("\nPatient created successfully\n")

def NameEdit(id,connection,cursor):
    NewName = input("Enter the corrected name of patient: ")
    cursor.execute("update patient set name='{}' where PatientId={}".format(NewName,id))
    connection.commit()
    print("\n patient name updated successfully \n")

def AgeEdit(id,connection,cursor):
    NewAge = input("Enter the corrected age of patient: ")
    cursor.execute("update patient set age={} where PatientId={}".format(NewAge,id))
    connection.commit()
    print("\n patient age updated successfully \n")

def PhoneNumberEdit(id,connection,cursor):
    NewNumber = int(input("Enter the corrected phone number of patient: "))
    cursor.execute("update patient set phnnumber={} where PatientId={}".format(NewNumber,id))
    connection.commit()
    print("\n patient phone number updated successfully \n")

def DeptEdit(id,connection,cursor):
    NewDept = input("Enter the corrected department name : ")
    cursor.execute("update patient set consuldept='{}' where PatientId={}".format(NewDept,id))
    connection.commit()
    print("\n patient consulting department updated successfully \n")

def DocEdit(id,connection,cursor):
    NewDoc = input("Enter the corrected doctor name : ")
    cursor.execute("update patient set consuldoc='{}' where PatientId={}".format(NewDoc,id))
    connection.commit()
    print("\n patient consulting doctor updated successfully \n")

def EditPatient(connection,cursor):
    id = int(input("Enter the PatientId: \n"))
    while True:
        lst = []
        print("Edit The Details Of Patient...")
        cursor.execute('select * from patient')
        for i in cursor:
            lst.append(i[0])
        #print(lst)    
        if id not in lst:
            print("enter a valid id")
            continue
        print("1. Edit Patient Name")
        print("2. Edit Patient age")
        print("3. Edit Patient Phone Number")
        print("4. Edit Consulting Department")
        print("5. Edit Consulting Doctor")
        print("6. Go Back")
        y = int(input("Enter Your Choice: "))
        match y:
            case 1:
                NameEdit(id,connection,cursor)
            case 2:
                AgeEdit(id,connection,cursor)
            case 3:
                PhoneNumberEdit(id,connection,cursor)
            case 4:
                DeptEdit(id,connection,cursor)
            case 5:
                DocEdit(id,connection,cursor)
            case 6:
                break
            case default:
                print("You Entered The Wrong Choice.")


def DeletePatient(connection,cursor):
    id = int(input("enter the id of patient to be deleted: \n"))
    lst = []
    
    cursor.execute('select * from patient')
    for j in cursor:
        lst.append(j[0])
    print("\n deleting the details of the patient \n")
    if id not in lst:
        print("\n enter a valid id \n")
    
    cursor.execute("delete from patient where PatientId={}".format(id))
    connection.commit()
    print("\n deletion is successful \n")   


def ViewPatient(connection,cursor):
    id = int(input("enter the id of patient to be viewed: \n"))
    lst = []
    cursor.execute('select * from patient')
    for k in cursor:
        lst.append(k[0])
    print(("viewing the details of patient\n"))
    if id not in lst:
        print(("enter a valid id\n"))
    cursor.execute("select * from patient where PatientId={}".format(id))
    print("patientid\tpatientname\tage\tphone number\tdepartment consulted\tdoctor consulted\n")
    for i in cursor:
        print("{}\t\t{}\t\t{}\t{}\t{}\t\t\t{}\n".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print("\n details are displayed successfully \n")


def Patient(connection,cursor):
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
                InsertPatient(connection,cursor)

            case 2:
                EditPatient(connection,cursor)

            case 3:
                DeletePatient(connection,cursor)

            case 4:    
                ViewPatient(connection,cursor)
                
            case 5:
                break



    