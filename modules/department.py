def InsertDetails(connection,cursor):
    DepartmentId = int(input("enter the department id: \n"))
    DepartmentName = input("enter the department name : \n")
    cursor.execute("insert into department values({},'{}')".format(DepartmentId,DepartmentName))
    connection.commit()
    print("Details entered successfully!!!")


def DeptNameEdit(DepartmentId,connection,cursor):
    newdeptname = input("enter the new name of department: \n")
    cursor.execute("update department set department='{}' where deptid={}".format(newdeptname,DepartmentId))
    connection.commit()
    print("\n patient consulting department updated successfully \n")

    k = int(input("Press 1 to Exit\n"))
    if k==1:
        Department(connection,cursor)

def EditDetails(connection,cursor):
    while True:
        print("Edit Department Details...")
        cursor.execute('select * from department')
        dataz = cursor.fetchall()
        print("departmentid\tdepartmentname\n")
        for i in dataz:
            print("{}\t\t{}\n".format(i[0],i[1]))
        departmentid = int(input("enter the department id for editing: \n"))
        print("1. Edit the name of department\n")
        print("2. Go Back\n")
        a = int(input("enter your choice: \n"))
        match a:
            case 1:
                DeptNameEdit(departmentid,connection,cursor)
            case 2:
                break
            case default:
                print("You entered the wrong choice")

def DeleteDetails(connection,cursor):
    while True:
        print("Delete Department......\n")
        cursor.execute('select * from department')
        datas = cursor.fetchall()
        print("departmentid\tdepartmentname\n")
        for i in datas:
            print("{}\t\t{}\n".format(i[0],i[1]))
        id = int(input("enter the id of department to be deleted: \n"))
        lst = []
        cursor.execute('select * from patient')
        for j in cursor:
            lst.append(j[0])
        print("\n deleting the details of the patient \n")
        if id not in lst:
            print("\n Sorry, enter a valid id \n")
            x = int(input("Press 1 to go back to main menu !!\n"))
            if x==1:
                break
            continue
        cursor.execute('delete from department where deptid={}'.format(id))
        connection.commit()
        print("\nDeletion is successfull\n")
        break

def Department(connection,cursor):
    while True:
        print("****** DEPARTMENT ******")
        print("1. Insert Details" )
        print("2. Edit Details" )
        print("3. Delete Details" )
        print("4. View Details" )
        print("5. Go Back" )

        x = int(input("enter your choice: \n"))
        match x:
            case 1:
                InsertDetails(connection,cursor)
            case 2:
                EditDetails(connection,cursor)
            case 3:
                DeleteDetails(connection,cursor)
            case 4:
                break
