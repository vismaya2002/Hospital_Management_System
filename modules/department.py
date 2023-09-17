from rich.console import Console
from rich.table import Table

console = Console()

def Enter():
    print('\n')

def InsertDetails(connection,cursor):
    DepartmentId = int(input("Enter the Department Id: \n"))
    DepartmentName = input("Enter the Department Name : \n")
    cursor.execute("insert into department values({},'{}')".format(DepartmentId,DepartmentName))
    connection.commit()
    console.print("\nDetails entered successfully!!!\n",style='bold')


def DeptNameEdit(DepartmentId,connection,cursor):
    newdeptname = input("Enter the Edited Name of Department: \n")
    cursor.execute("update department set department='{}' where deptid={}".format(newdeptname,DepartmentId))
    connection.commit()
    console.print("\n Consulting Department Updated Successfully !!!\n",style='bold')

    k = int(input("Press 1 to Exit\n"))
    if k==1:
        return

def EditDetails(connection,cursor):
    while True:
        console.print("\nEdit Department Details...\n",style='bold')
        table = Table(title="DEPARTMENTS")
        row = []
        cursor.execute('select * from department')
        dataz = cursor.fetchall()
        column = ["Department Id","Department Name"]
        for i in dataz:
            temprow = (str(i[0]),i[1])
            row.append(temprow)
        for column in column:
            table.add_column(column,style="cyan")
        for row in row:
            table.add_row(*row, style='magenta')
        console.print(table)
        departmentid = int(input("Enter the Department Id for Editing: \n"))

        Enter()
        tables = Table(title="EDITION MENU")
        tables.add_column("S. No.", style="cyan", no_wrap=True)
        tables.add_column("Options", style="magenta")
        tables.add_row("1", "Edit the Name of Department")
        tables.add_row("2", "Go Back")
        console.print(tables)
        Enter()

        a = int(input("Enter Your Choice: \n"))
        match a:
            case 1:
                DeptNameEdit(departmentid,connection,cursor)
                break
            case 2:
                break
            case default:
                console.print("\nYou entered the wrong choice\n",style='bold red')

def DeleteDetails(connection,cursor):
    while True:
        console.print("Delete Department......\n",style='bold')
        table = Table(title= "DEPARTMENTS")
        row = []
        cursor.execute('select * from department')
        datas = cursor.fetchall()
        column = ["Department Id","Department Name"]
        for i in datas:
            temprows = (str(i[0]),i[1])
            row.append(temprows)
        for column in column:
            table.add_column(column,style="cyan")
        for row in row:
            table.add_row(*row, style='magenta')
        console.print(table)
        id = int(input("Enter the Id of Department to be Deleted: \n"))
        lst = []
        cursor.execute('select * from department')
        for j in cursor:
            lst.append(j[0])
        console.print("\n Deleting Department \n",style='bold')
        if id not in lst:
            console.print("\n Sorry, enter a valid id \n",style='bold red')
            x = int(input("Press 1 to go back to main menu !!\n"))
            if x==1:
                break
            continue
        cursor.execute('delete from department where deptid={}'.format(id))
        connection.commit()
        console.print("\nDeletion is Successfull\n",style='bold red')
        break

def ViewDetails(connection,cursor):
    console.print("\nViewing the Department Details\n",style='bold')
    table = Table(title="DEPARTMENT")
    row = []
    cursor.execute('select * from department')
    data = cursor.fetchall()
    column = ["Department Id","Department Name"]
    for i in data:
        temprow = [str(i[0]),i[1]]
        row.append(temprow)
    for column in column:
        table.add_column(column,style="cyan")
    for row in row:
        table.add_row(*row, style='magenta')
    console.print(table)
    input("Press any Key to Continue !!!\n")

def Department(connection,cursor):
    while True:

        Enter()

        table = Table(title="DEPARTMENT")

        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")

        table.add_row("1", "Insert Department")
        table.add_row("2", "Edit Department")
        table.add_row("3", "Delete Department")
        table.add_row("4", "View Department Details")
        table.add_row("5", "Go Back")

        console.print(table)

        Enter()

        x = int(input("Enter Your Choice: \n"))
        match x:
            case 1:
                InsertDetails(connection,cursor)
            case 2:
                EditDetails(connection,cursor)
            case 3:
                DeleteDetails(connection,cursor)
            case 4:
                ViewDetails(connection,cursor)
            case 5:
                break
