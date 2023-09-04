def InsertDoctor(connection,cursor):
    cursor.execute('select * from department')
    dataz = cursor.fetchall()
    print("departmentid\tdepartmentname\n")
    for i in dataz:
        print("{}\t\t{}\n".format(i[0],i[1]))
    cursor.execute('select * from doctor')
    val = cursor.fetchall()
    id = len(val)+10001    
    name = input("Enter the name of doctor:  \n")
    age = int(input("Enter the age of doctor: \n"))
    deptid = int(input("Enter the department of doctor: \n"))
    qualific = input("Enter the qualification of the doctor: \n")
    phnnumber = int(input("enter the phone number of doctor: \n"))
    cursor.execute("insert into doctor values({},'{}',{},'{}','{}',{})".format(id,name,age,deptid,qualific,phnnumber))
    connection.commit()
    print("\nDoctor created successfully\n")


def NameEdit(id,connection,cursor):
    newname = input("enter the new name of doctor: \n")
    cursor.execute("update doctor set name='{}' where doctorid={}".format(newname,id))
    connection.commit()
    print("\n Doctor name updated successfully \n")

def AgeEdit(id,connection,cursor):
    newage = input("enter the new age of doctor: \n")
    cursor.execute("update doctor set age={} where doctorid={}".format(newage,id))
    connection.commit()
    print("\n Doctor age updated successfully \n")

def Deptedit(id,connection,cursor):
    newdept = int(input("enter the new departmentid : \n"))
    cursor.execute("update doctor set deptid={} where doctorid={}".format(newdept,id))
    connection.commit()
    print("\n Doctor department id updated successfully \n")

def Qualifedit(id,connection,cursor):
    newqualifi = input("enter the new qualifications: \n")
    cursor.execute("update doctor set qualification='{}' where doctorid={}".format(newqualifi,id))
    connection.commit()
    print("\n Doctor qualification updated successfully \n")

def Phnedit(id,connection,cursor):
    newphn = input("enter the new phone number of doctor: \n")
    cursor.execute("update doctor set phnnumber={} where doctorid={}".format(newphn,id))
    connection.commit()
    print("\n Doctor phn number updated successfully \n")


def EditDoctor(connection,cursor):
    while True:
        print("Edit The Details of Doctor...")
        id = int(input("enter the id of doctor \n"))
        print("1. Enter the edited name of doctor \n")
        print("2. Enter the edited age of doctor \n")
        print("3. Enter the edited department of doctor \n")
        print("4. Enter the edited qualification of doctor \n")
        print("5. Enter the edited phone number of doctor \n")
        y = int(input("Enter your choice: \n"))
        match y:
            case 1:
                NameEdit(id,connection,cursor)
            case 2:
                AgeEdit(id,connection,cursor)
            case 3:
                Deptedit(id,connection,cursor)
            case 4:
                Qualifedit(id,connection,cursor)
            case 5:
                Phnedit(id,connection,cursor)
            case 6:
                break
            case default:
                print("You Entered The Wrong Choice.")

def Doctor(connection,cursor):
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
                InsertDoctor(connection,cursor)
            case 2:
                EditDoctor(connection,cursor)
            case 3:
                break