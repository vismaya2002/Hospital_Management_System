import mysql.connector as msc
from typing import Final
from os import getenv
from dotenv import load_dotenv,find_dotenv

from modules import *

load_dotenv(find_dotenv())

MYSQL_HOST: Final = getenv("MYSQL_HOST")
MYSQL_PORT: Final = getenv("MYSQL_PORT")
MYSQL_USER: Final = getenv("MYSQL_USER")
MYSQL_PASSWORD: Final = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE: Final = getenv("MYSQL_DATABASE")
CREATE_TABLE: Final = getenv("CREATE_TABLE",True)

def main():

    connection = msc.connect(host = MYSQL_HOST,port = MYSQL_PORT , user=MYSQL_USER, passwd=MYSQL_PASSWORD, database=MYSQL_DATABASE)
    cursor = connection.cursor()
    if connection.is_connected():
        print("Database Connected.")
   
    while True:

        print("******* WELCOME TO HOSPITAL MANAGEMENT SYSTEM *******")
        print("1. Patient Details")
        print("2. Doctor Details")
        print("3. Department Details")
        print("4. Non-Consulting staff Details")
        print("5. Staff Details")
        print("6. Exit")
        x = int(input("Enter Your Choice : "))
        match x:
            case 1:
                Patient(connection,cursor)
            case 2:
                Doctor(connection,cursor)
            
            case 6:
                break
    

if __name__ == '__main__':
    main()
