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
    print("\n patient name updated successfully \n")

def AgeEdit():
    newage = input("enter the new age of doctor: \n")

def deptedit():
    newdept = input("enter the new department: \n")

def qualifedit():
    newqualifi = input("enter the new qualifications: \n")

def phnedit():
    newphn = input("enter the new phone number of doctor: \n")


def EditDoctor(connection,cursor):
    while True:
        print("Edit The Details of Doctor...")
        id = int(input("enter the id of doctor: \n"))
        print("1. Enter the edited name of doctor: \n")
        print("2. Enter the edited age of doctor: \n")
        print("3. Enter the edited department of doctor: \n")
        print("4. Enter the edited qualification of doctor: \n")
        print("5. Enter the edited phone number of doctor: \n")
        y = int(input("Enter your choice: \n"))
        match y:
            case 1:
                NameEdit(id,connection,cursor)
            case 2:
                break

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
                EditDoctor()
                
            case 5:
                break