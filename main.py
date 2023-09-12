import mysql.connector as msc
from typing import Final
from os import getenv
from dotenv import load_dotenv,find_dotenv

from modules import *

from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()

load_dotenv(find_dotenv())

MYSQL_HOST: Final = getenv("MYSQL_HOST")
MYSQL_PORT: Final = getenv("MYSQL_PORT")
MYSQL_USER: Final = getenv("MYSQL_USER")
MYSQL_PASSWORD: Final = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE: Final = getenv("MYSQL_DATABASE")
CREATE_TABLE: Final = getenv("CREATE_TABLE",True)

def Enter():
    print('\n')

def main():
    Enter()
    with console.status("[bold green]Connecting to database..") as status:
        sleep(2)
        connection = msc.connect(host = MYSQL_HOST,port = MYSQL_PORT , user=MYSQL_USER, passwd=MYSQL_PASSWORD, database=MYSQL_DATABASE)
        cursor = connection.cursor()
        if connection.is_connected():
            console.log(f'[bold][green]Database Connected.')
   
    while True:

        Enter()

        table = Table(title="HOSPITAL MANAGEMENT SYSTEM")

        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")

        table.add_row("1", "Patient")
        table.add_row("2", "Doctor")
        table.add_row("3", "Department")
        table.add_row("4", "Non-Consulting Staff")
        table.add_row("5", "Staff")
        table.add_row("6", "Exit")

        console.print(table)

        Enter()

        x = int(input("Enter Your Choice : "))
        match x:
            case 1:
                Patient(connection,cursor)
            case 2:
                Doctor(connection,cursor)
            case 3:
                Department(connection,cursor)
            case 6:
                break
    

if __name__ == '__main__':
    main()
