from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich import print
from rich.style import Style

console = Console()

def Enter():
    print('\n')

def InsertPatient(connection,cursor):
    cursor.execute('select * from patient')
    val = cursor.fetchall()
    if len(val)==0:
        id = 101
    else:
        id = val[-1][0]+1
    name = input("Enter the name of patient : \n")
    age = int(input("Enter the age of patient : \n"))
    PhnNumber = int(input("Enter the phone number of patient : \n"))
    table = Table(title="DEPARTMENTS")
    cursor.execute('select * from department order by department')
    columns = ["Department Id","Department Name"]
    rows = []
    for x in cursor:
        temprow = [str(x[0]),x[1]]
        rows.append(temprow)
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='black')
    console = Console()
    console.print(table)
    ConsultingDepartment = int(input("Enter the departmentid to be consulted : \n"))
    cursor.execute("select deptid,doctorid,name,qualification from doctor where deptid={}".format(ConsultingDepartment))
    print("DepartmentId\tDoctorId\tName\tQualification\n")
    for z in cursor:
        print("{}\t\t{}\t\t{}\t\t{}".format(z[0],z[1],z[2],z[3]))
    ConsulitngDoctor = int(input("Enter the id of doctor consulting : \n"))
    cursor.execute("insert into patient values({},'{}',{},{},{},{})".format(id,name,age,PhnNumber,ConsultingDepartment,ConsulitngDoctor))
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
    NewDept = int(input("Enter the corrected department name : "))
    cursor.execute("update patient set consuldept={} where PatientId={}".format(NewDept,id))
    connection.commit()
    print("\n patient consulting department updated successfully \n")

def DocEdit(id,connection,cursor):
    NewDoc = int(input("Enter the corrected doctor id : "))
    cursor.execute("update patient set consuldoc={} where PatientId={}".format(NewDoc,id))
    connection.commit()
    print("\n patient consulting doctor updated successfully \n")

def EditPatient(connection,cursor):
    
    while True:
        id = int(input("Enter the PatientId: \n"))
        cursor.execute("select * from patient where PatientId={}".format(id))
        print("patientid\tpatientname\tage\tphone number\tdepartment consulted\tdoctor consulted\n")
        for i in cursor:
            print("{}\t\t{}\t\t{}\t{}\t{}\t\t\t{}\n".format(i[0],i[1],i[2],i[3],i[4],i[5]))
        lst = []
        print("Edit The Details Of Patient...")
        cursor.execute('select * from patient')
        for i in cursor:
            lst.append(i[0])
        #print(lst)    
        if id not in lst:
            print("enter a valid PatientId")
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
    while True:
        id = int(input("enter the id of patient to be deleted: \n"))
        cursor.execute("select * from patient where PatientId={}".format(id))
        print("patientid\tpatientname\tage\tphone number\tdepartment consulted\tdoctor consulted\n")
        for i in cursor:
            print("{}\t\t{}\t\t{}\t{}\t{}\t\t\t{}\n".format(i[0],i[1],i[2],i[3],i[4],i[5]))
        lst = []
        cursor.execute('select * from patient')
        for j in cursor:
            lst.append(j[0])
        if id not in lst:
            print("\n enter a valid id \n")
            x = int(input("Press 1 to go back to main menu !!\n"))
            if x==1:
                break
            continue
        x = int(input("Press 1 if you want to delete...\n"))
        if x==1:
            print("\n deleting the details of the patient \n")
            cursor.execute("delete from patient where PatientId={}".format(id))
            connection.commit()
            print("\n deletion is successful \n")   
            break
        else:
            print("[bold red]Sorry, Incorrect Request.[/bold red]")
            break
        
        

def ViewPatient(connection,cursor):
    id = int(input("enter the id of patient to be viewed: \n"))
    lst = []
    cursor.execute('select * from patient')
    for k in cursor:
        lst.append(k[0])
    print(("viewing the details of patient\n"))
    if id not in lst:
        print(("[bold red]Sorry, enter a valid id[bold red]\n"))
        return
    table = Table(title="PATIENT DETAILS")
    cursor.execute("select patient.PatientId,patient.name,patient.age,patient.phone_number,patient.department_id,doctor.doctorid,doctor.name from patient,doctor where patient.doctor_id=doctor.doctorid and PatientId={}".format(id))
    columns = ["Patient Id","Patient Name","Age","Phone Number","Department Consulted","Doctor Id","Doctor Consulted"]
    rows = []
    for i in cursor:
        temprow =[str(i[0]),i[1],str(i[2]),str(i[3]),str(i[4]),str(i[5]),i[6]]
        rows.append(temprow)
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='white')
    console=Console()
    console.print(table)
    console.print("\n details are displayed successfully \n" , style="bold")


def Patient(connection,cursor):
    while True:

        Enter()

        table = Table(title="PATIENT ")

        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")

        table.add_row("1", "Insert Patient")
        table.add_row("2", "Edit Patient")
        table.add_row("3", "Delete Patient")
        table.add_row("4", "View Patient Details")
        table.add_row("5", "Go Back")

        console.print(table)

        Enter()
        
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



    