def InsertDetails(connection,cursor):
    DepartmentId = int(input("enter the department id: \n"))
    DepartmentName = input("enter the department name : \n")
    cursor.execute("insert into department values({},'{}')".format(DepartmentId,DepartmentName))
    connection.commit()
    print("Details entered successfully!!!")

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
                
                break
