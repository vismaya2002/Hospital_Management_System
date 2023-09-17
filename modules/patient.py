from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich import print
from rich.style import Style
from time import sleep

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
        table.add_column(column,style="cyan")
    for row in rows:
        table.add_row(*row, style='magenta')
    console = Console()
    console.print(table)
    ConsultingDepartment = int(input("Enter the departmentid to be consulted : \n"))
    tables = Table(title="DOCTOR DETAILS")
    srow = []
    cursor.execute("select deptid,doctorid,name,qualification from doctor where deptid={}".format(ConsultingDepartment))
    scolumn = ["Department Id","Doctor Id","Name","Qualification"]
    for z in cursor:
        temprows = [str(z[0]),str(z[1]),z[2],z[3]]
        srow.append(temprows)
    for column in scolumn:
        tables.add_column(column,style="cyan")
    for row in srow:
        tables.add_row(*row, style='magenta')
    console = Console()
    console.print(tables)
    ConsulitngDoctor = int(input("Enter the id of doctor consulting : \n"))
    cursor.execute("insert into patient values({},'{}',{},{},{},{})".format(id,name,age,PhnNumber,ConsultingDepartment,ConsulitngDoctor))
    connection.commit()
    console.print("\nPatient Created Successfully!!!\n",style='bold')

def NameEdit(id,connection,cursor):
    NewName = input("Enter the Corrected Name of Patient: ")
    cursor.execute("update patient set name='{}' where PatientId={}".format(NewName,id))
    connection.commit()
    console = Console()
    console.print("\n Patient Name Updated Successfully !!!\n",style='bold')
    

def AgeEdit(id,connection,cursor):
    NewAge = input("Enter the Corrected Age of Patient: ")
    cursor.execute("update patient set age={} where PatientId={}".format(NewAge,id))
    connection.commit()
    console = Console()
    console.print("\n Patient Age Updated Successfully !!!\n",style='bold')
    

def PhoneNumberEdit(id,connection,cursor):
    NewNumber = int(input("Enter the Corrected Phone Number of Patient: "))
    cursor.execute("update patient set phone_number={} where PatientId={}".format(NewNumber,id))
    connection.commit()
    console = Console()
    console.print("\n Patient Phone Number Updated Successfully !!!\n",style='bold')
    

def DeptEdit(id,connection,cursor):
    NewDept = int(input("Enter the Corrected Department Name : "))
    cursor.execute("update patient set consuldept={} where PatientId={}".format(NewDept,id))
    connection.commit()
    console = Console()
    console.print("\n Patient Consulting Department Updated Successfully !!!\n",style='bold')
    
def DocEdit(id,connection,cursor):
    NewDoc = int(input("Enter the Corrected Doctor Id : "))
    cursor.execute("update patient set consuldoc={} where PatientId={}".format(NewDoc,id))
    connection.commit()
    console = Console()
    console.print("\n Patient Consulting Doctor Updated Successfully !!!\n",style='bold')
    

def EditPatient(connection,cursor):
    
    while True:
        id = int(input("Enter the PatientId: \n"))
        table = Table(title="DEPARTMENTS")
        row = []
        cursor.execute("select * from patient where PatientId={}".format(id))
        datas = cursor.fetchall()
        console = Console()
        if id not in datas:
            console.print("\n Sorry, enter a valid id \n",style='bold red')
            x = int(input("Press 1 to go back to main menu !!\n"))
            if x==1:
                break
        column = ["Patient Id","Patient Name","Age","Phone Number","Department Consulted","Doctor Consulted"]
        for i in datas:
            temprow = [str(i[0]),i[1],str(i[2]),str(i[3]),str(i[4]),str(i[5])]
            row.append(temprow)
        for column in column:
            table.add_column(column,style="cyan")
        for row in row:
            table.add_row(*row, style='magenta')
        console.print(table)
        lst = []
        console.print("Edit The Details Of Patient...",style='bold')
        cursor.execute('select * from patient')
        for i in cursor:
            lst.append(i[0])
        #print(lst)    
        
            
        Enter()
        tables = Table(title="EDITION MENU")
        tables.add_column("S. No.", style="cyan", no_wrap=True)
        tables.add_column("Options", style="magenta")

        tables.add_row("1.","Edit Patient Name")
        tables.add_row("2.","Edit Patient age")
        tables.add_row("3.","Edit Patient Phone Number")
        tables.add_row("4.","Edit Consulting Department")
        tables.add_row("5.","Edit Consulting Doctor")
        tables.add_row("6.","Go Back")
        console.print(tables)
        Enter()

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
                console.print("You Entered The Wrong Choice.",style='bold red')


def DeletePatient(connection,cursor):
    while True:
        id = int(input("Enter The Id Of Patient To Be Deleted: \n"))
        table = Table(title="PATIENT DETAILS")
        row = []
        cursor.execute("select * from patient where PatientId={}".format(id))
        dataz = cursor.fetchall()
        if id not in dataz[0]:
            print("\n[bold red] Enter a Valid Id [/bold red]\n")
            x = int(input("Press 1 To Go Back To Main Menu !!!\n"))
            if x==1:
                break
            continue

        column = ["Patient Id","Patient Name","Age","Phone Number","Department Consulted","Doctor Consulted"]
        for i in dataz:
            temprow = [str(i[0]),i[1],str(i[2]),str(i[3]),str(i[4]),str(i[5])]
            row.append(temprow)
        for column in column:
            table.add_column(column,style="cyan")
        for row in row:
            table.add_row(*row, style='magenta')
        console = Console()
        console.print(table)
        lst = []
        cursor.execute('select * from patient')
        for j in cursor:
            lst.append(j[0])
        x = input("\nPress 1 if you want to DELETE... Else Press any other Key \n")
        if x=='1':
            console.print("\n Deleting The Details Of The Patient... \n",style='bold')
            sleep(2)
            cursor.execute("delete from patient where PatientId={}".format(id))
            connection.commit()
            console.print("\n Deletion Is Successful... \n",style='bold')   
            sleep(2)
            break
        else:
            print("[bold red]Request Aborted.[/bold red]")
            sleep(2)
            break
        
        

def ViewPatient(connection,cursor):
    id = int(input("enter the id of patient to be viewed: \n"))
    lst = []
    console=Console()
    cursor.execute('select * from patient')
    for k in cursor:
        lst.append(k[0])
    console.print("Viewing the Details of Patient\n",style='bold')
    sleep(2)
    if id not in lst:
        print(("[bold red]Sorry, enter a valid id[bold red]\n"))
        sleep(2)
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
    console.print(table)
    console.print("\n Details are Displayed Successfully \n" , style="bold")


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



    