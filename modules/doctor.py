from rich.console import Console
from rich.table import Table


def InsertDoctor(connection,cursor):
    table = Table(title="DEPARTMENT")
    cursor.execute('select * from department order by department')
    dataz = cursor.fetchall()
    columns = ['Department Id','Department Name']
    rows = []
    for i in dataz:
        temprow = [str(i[0]),i[1]]
        rows.append(temprow)
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='black')
    console = Console()
    console.print(table)
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
        lst = []
        cursor.execute('select * from doctor')
        for i in cursor:
            lst.append(i[0])
        #print(lst)    
        if id not in lst:
            print("enter a valid DoctorId")
            z = int(input("Press 1 to go back to main menu..."))
            if z==1:
                Doctor(connection,cursor)
            else:
                break
        print("1. Edit name of doctor \n")
        print("2. Edit age of doctor \n")
        print("3. Edit department of doctor \n")
        print("4. Edit qualification of doctor \n")
        print("5. Edit phone number of doctor \n")
        y = int(input("Enter your choice: \n"))
        match y:
            case 1:
                NameEdit(id,connection,cursor)
                break
            case 2:
                AgeEdit(id,connection,cursor)
                break
            case 3:
                Deptedit(id,connection,cursor)
                break
            case 4:
                Qualifedit(id,connection,cursor)
                break
            case 5:
                Phnedit(id,connection,cursor)
                break
            case 6:
                break
            case default:
                print("You Entered The Wrong Choice.")

def DeleteDoctor(connection,cursor):
    while True:
        id = int(input("enter id of doctor to be deleted:\n"))
        cursor.execute("select * from doctor where doctorid={}".format(id))
        table = Table(title="DOCTOR DETAILS")
        columns = ["Doctor Id","Doctor Name","Age","Department Id","Qualification","Phone Number"]
        rows = []
        for i in cursor:
            temprow = [str(i[0]),i[1],str(i[2]),str(i[3]),i[4],str(i[5])]
            rows.append(temprow)
        for column in columns:
            table.add_column(column)
        for row in rows:
            table.add_row(*row, style='black')
        console = Console()
        console.print(table)
        lst = []
        cursor.execute('select * from doctor')
        for i in cursor:
            lst.append(i[0])
        if id not in lst:
            print("\n enter a valid id \n")
            x = input("Press 1 to go back to main menu !!\n")
            if x=='1':
                break
            continue
        x = int(input("Press 1 if you want to delete...\n"))
        if x==1:
            print("deleting the details of doctor")
            cursor.execute("delete from doctor where doctorid={}".format(id))
            connection.commit()
            print("\n deletion is successful \n")   
            break
        else:
            print("Incorrect Request...")
            break

def ViewDoctor(connection,cursor):
    id = int(input("enter the id of doctor to be viewed: \n"))
    lst = []
    l = []
    cursor.execute('select * from doctor')
    for j in cursor:
        lst.append(j[0])
    table = Table(title="DOCTOR DETAILS")
    if id in lst:
        cursor.execute('select department.department,department.deptid,doctor.doctorid,doctor.name,doctor.age,doctor.qualification,doctor.phnnumber from department,doctor where department.deptid=doctor.deptid and doctorid={}'.format(id))
        for i in cursor:
            l.append(i)
        print(("Viewing the details of doctor\n"))
        rows = []
        columns = ["Department Name","Department Id","Doctor Id","Name","Age","Qualification","Phone Number"]
        for i in l:
            temprow = [i[0],str(i[1]),str(i[2]),i[3],str(i[4]),i[5],str(i[6])]
            rows.append(temprow)
        for column in columns:
            table.add_column(column)
        for row in rows:
            table.add_row(*row, style='black')
        console = Console()
        console.print(table)
        print("\n details are displayed successfully \n")
    else:
        print(("enter a valid id\n"))
        

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
                DeleteDoctor(connection,cursor)
            case 4:
                ViewDoctor(connection,cursor)
            case 5:
                break