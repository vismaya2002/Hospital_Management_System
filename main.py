from modules import *
def main():
   
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
                Patient()
                
            case 6:
                break
    

if __name__ == '__main__':
    main()
