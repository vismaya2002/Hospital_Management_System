from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()

def Enter():
    print('\n')


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
        table.add_column(column,style='cyan')
    for row in rows:
        table.add_row(*row, style='magenta')
    console = Console()
    console.print(table)
    cursor.execute('select * from doctor')
    val = cursor.fetchall()
    if len(val)==0:
        id = 10001
    else:
        id = val[-1][0]+1
    name = input("Enter the Name of Doctor:  \n")
    age = int(input("Enter the Age of Doctor: \n"))
    deptid = int(input("Enter the Department Id of Doctor: \n"))
    qualific = input("Enter the Qualification of the Doctor: \n")
    phnnumber = int(input("Enter the Phone Number of Doctor: \n"))
    cursor.execute("insert into doctor values({},'{}',{},'{}','{}',{})".format(id,name,age,deptid,qualific,phnnumber))
    connection.commit()
    console.print("\nDoctor Created Successfully !!!\n",style='bold')
    sleep(1)


def NameEdit(id,connection,cursor):
    newname = input("Enter the Edited Name of Doctor: \n")
    cursor.execute("update doctor set name='{}' where doctorid={}".format(newname,id))
    connection.commit()
    console = Console()
    console.print("\n Doctor Name Updated Successfully !!!\n",style='bold')
    sleep(1)

def AgeEdit(id,connection,cursor):
    newage = input("Enter the Edited Age of Doctor: \n")
    cursor.execute("update doctor set age={} where doctorid={}".format(newage,id))
    connection.commit()
    console = Console()
    console.print("\n Doctor Age Updated Successfully !!!\n",style='bold')
    sleep(1)

def Deptedit(id,connection,cursor):
    newdept = int(input("Enter the Edited Department Id : \n"))
    cursor.execute("update doctor set deptid={} where doctorid={}".format(newdept,id))
    connection.commit()
    console = Console()
    console.print("\n Doctor Department Id Updated Successfully !!!\n",style='bold')
    sleep(1)

def Qualifedit(id,connection,cursor):
    newqualifi = input("Enter the Edited Qualifications: \n")
    cursor.execute("update doctor set qualification='{}' where doctorid={}".format(newqualifi,id))
    connection.commit()
    console = Console()
    console.print("\n Doctor Qualification Updated Successfully !!!\n",style='bold')
    sleep(1)

def Phnedit(id,connection,cursor):
    newphn = input("Enter the Edited Phone Number of Doctor: \n")
    cursor.execute("update doctor set phnnumber={} where doctorid={}".format(newphn,id))
    connection.commit()
    console = Console()
    console.print("\n Doctor Phone Number Updated Successfully !!!\n",style='bold')
    sleep(1)


def EditDoctor(connection,cursor):
    while True:
        console = Console()
        console.print("\nEdit The Details of Doctor...\n",style='bold')
        sleep(1)
        id = int(input("Enter the Id of Doctor \n"))
        table = Table(title="DOCTOR DETAILS")
        row = []
        cursor.execute("select * from doctor where doctorid={}".format(id))
        datas = cursor.fetchall()
        if id not in datas:
            console.print("\n Sorry, enter a valid id \n",style='bold red')
            x = int(input("Press 1 to go back to main menu !!\n"))
            if x==1:
                break
        column = ["Doctor Id","Doctor Name","Age","Department Id","Qualification","Phone Number"]
        for i in cursor:
            temprow = [str(i[0]),i[1],str(i[2]),str(i[3]),i[4],str(i[5])]
            row.append(temprow)
        for column in column:
            table.add_column(column,style="cyan")
        for row in row:
            table.add_row(*row, style='magenta')
        console = Console()
        console.print(table)
        
        Enter()
        tables = Table(title="EDITION MENU")

        tables.add_column("S. No.", style="cyan", no_wrap=True)
        tables.add_column("Options", style="magenta")

        tables.add_row("1", "Edit Name of Doctor ")
        tables.add_row("2", "Edit Age of Doctor ")
        tables.add_row("3", "Edit department of doctor ")
        tables.add_row("4", "Edit qualification of doctor ")
        tables.add_row("5", "Edit phone number of doctor")
        tables.add_row("6", "Go Back")
        console.print(tables)
        Enter()


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
        id = int(input("Enter Id of Doctor to be Deleted:\n"))
        console = Console()
        cursor.execute("select * from doctor where doctorid={}".format(id))
        datas = cursor.fetchall()
        if id not in datas[0]:
            console.print("\n Enter a Valid Id \n",style='bold red')
            k = input("Press 1 to go Back to Main Menu !!\n")
            if k=='1':
                break
            continue
        table = Table(title="DOCTOR DETAILS")
        columns = ["Doctor Id","Doctor Name","Age","Department Id","Qualification","Phone Number"]
        rows = []
        for i in datas:
            temprow = [str(i[0]),i[1],str(i[2]),str(i[3]),i[4],str(i[5])]
            rows.append(temprow)
        for column in columns:
            table.add_column(column,style='cyan')
        for row in rows:
            table.add_row(*row, style='magenta')
        
        console.print(table)
        x = input("Press 1 if you want to delete...\n")
        if x=='1':
            console.print("\nDeleting the Details of Doctor\n",style='bold')
            sleep(1)
            cursor.execute("delete from doctor where doctorid={}".format(id))
            connection.commit()
            console.print("\n Deletion is Successful \n",style='bold')   
            sleep(1)
            break
        else:
            console.print("Incorrect Request...",style='bold red')
            sleep(1)
            break

def ViewDoctor(connection,cursor):
    y = input("Press 1 if you want to view the details of the entire doctors OR 0 to view details of a single doctor...\n")
    doclist = []
    if y=='1':
        cursor.execute('select department.department,department.deptid,doctor.doctorid,doctor.name,doctor.age,doctor.qualification,doctor.phnnumber from department,doctor where department.deptid=doctor.deptid')
        datas = cursor.fetchall()
        for k in datas:
            doclist.append(k)
        tables = Table(title="DOCTOR DETAILS")
        srow = []
        scolumn = ["Department Name","Department Id","Doctor Id","Name","Age","Qualification","Phone Number"]
        for j in doclist:
            temprows = [j[0],str(j[1]),str(j[2]),j[3],str(j[4]),j[5],str(j[6])]
            srow.append(temprows)
        for column in scolumn:
            tables.add_column(column,style='cyan')
        for row in srow:
            tables.add_row(*row, style='magenta')
        console = Console()
        console.print(tables)
        input("Press any Key to Continue !!!\n")
    elif y== '0':

        id = int(input("Enter the Id of Doctor to be Viewed: \n"))
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
                table.add_column(column,style='cyan')
            for row in rows:
                table.add_row(*row, style='magenta')
            consoles = Console()
            consoles.print(table)
            consoles.print("\n Details are Displayed Successfully !!!\n",style='bold')
            sleep(1)
        else:
            consoles.print("\nEnter a Valid Id\n",style='bold red')
            sleep(1)
    else:
        consoles.print("\nInvalid Request...\n",style='bold red')
        sleep(1)
        
        

def Doctor(connection,cursor):
    while True:

        Enter()

        table = Table(title="DOCTOR")

        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")

        table.add_row("1", "Insert Doctor")
        table.add_row("2", "Edit Doctor")
        table.add_row("3", "Delete Doctor")
        table.add_row("4", "View Doctor Details")
        table.add_row("5", "Go Back")

        console.print(table)

        Enter()

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